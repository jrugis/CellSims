from __future__ import print_function
import os
import time
import shutil

import _my_sweep

##################################################################
# functions
##################################################################

# replace value in parameters file
def replace_pvalue(p, v):
  fin = open("cs.dat", 'r')
  fout = open("temp.dat", 'w')
  for line in fin:
    fout.write(line)
    if line[1:2] != '!':  # skip non-parameter lines
      continue
    p_names = line.split()[1:]
    if p in p_names:  # parameter in the line?
      p_values = fin.next().split();
      for i in range(len(p_names)):
        if p_names[i] == (p): 
          fout.write(str(v))  # replace the value
        else:
          fout.write(p_values[i])
        if i < (len(p_names) - 1):
          fout.write(' ')
      fout.write('\n')
  fin.close()
  fout.close()
  os.rename("temp.dat", "cs.dat")
  return

##################################################################
# main program
##################################################################

# get the user set parameters
platform, solver, mesh_type, model, parms, parmA, valsA, parmB, valsB = _my_sweep.sweep_parms()

# create the top level results directory
csdir = os.getcwd()

if not os.path.exists("results"):
    os.makedirs("results")
path = "results/CS" + time.strftime("%y%m%d%H%M%S")
os.mkdir(path)
os.chdir(path)
model_full = model + "_" + platform + "_" + solver
print("Cell Simulation:", model_full)

# on pan we create an empty file to store the paths to simulation directories and arguments
if platform == "pan":
    os.mkdir("slurm")
    fpan = open(os.path.join("slurm", "_pan_array.in"), "w")
    num_sims = 0  # counter for the total number of simulations

# iterate through seven cells and all the parameters
for cell in range(1, 8):
  path = str(cell)
  os.mkdir(path)
  os.chdir(path)
  mesh = "cell0" + str(cell) + mesh_type
  print(mesh)
  for v1 in valsA:
    for v2 in valsB:
      pdir = ""
      #for pv in parms:
      #  pdir += pv[0] + '-' + str(pv[1]) + '_'
      pdir += parmA + '-' + str(v1) + '_' + parmB + '-' + str(v2)
      pdir = pdir.replace('.', 'p')
      os.mkdir(pdir)
      os.chdir(pdir)

      # copy data files and execute the simulation
      os.system("cp " + csdir + "/meshes/" + mesh + ".msh cs.msh")
      os.system("cp " + csdir + "/parameters/" + model + ".dat cs.dat")
              
      for pv in parms: # set the fixed values
        replace_pvalue(pv[0], pv[1])
      replace_pvalue(parmA, v1) # set the swept values
      replace_pvalue(parmB, v2)

      if platform == "linux":
          NP_MAX = 20

          # wait if at maximum number of parallel processes
          while int(os.popen("ps | grep " + model + " | wc -l").read()) >= NP_MAX:
              time.sleep(1)

          # run a non-blocking simulation process
          print(pdir)
          os.system("bash " + csdir + "/linux.sh " + model_full + " " + model + " " + mesh + " " + csdir + " &")
          time.sleep(0.5) # wait until after startup memory useage peak
      elif platform == "pan":
          fpan.write(os.getcwd() + " " + model_full + " " + model + " " + mesh + " " + csdir + "\n")
          num_sims += 1
      else:
          print("ERROR: invalid platform -", platform)

      os.chdir("..")
  os.chdir("..")

# submit array job on pan
if platform == "pan":
    print("Submitting array job with {0} individual jobs".format(num_sims))
    fpan.close()
    os.chdir("slurm")

    # copy and edit slurm script
    with open(os.path.join(csdir, "run_sim.sl")) as fh:
        lines = fh.readlines()
    for i, line in enumerate(lines):
        if line.startswith("#SBATCH --array="):
            lines[i] = "#SBATCH --array=1-{0}\n".format(num_sims)
    with open("_run_sim.sl", "w") as fh:
        fh.write("".join(lines))

    # submit slurm script
    os.system("sbatch _run_sim.sl")

    os.chdir("..")

# go back to top level
os.chdir(csdir)
