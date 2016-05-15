import os
import time

platform = "linux"
#platform = "pan"

model = "generic3d_03"
mesh = "cell01m_HARMONIC_100p"

# fixed parameters
#parms = [["PLCds", 0.5], ["IPRdn", 0.5], ["IPRdf", 3.5]]
#parms = [["kRyR", 0.0]]
#parms = [["Dce", 5.0]]
parms = []

# 2D parameter sweep
#parmA = "Vdeg"
#valsA = [0.16, 0.18]
#parmB = "K3K"
#valsB = [0.4, 0.43]
parmA = "VPLC"
valsA = [0.01, 0.02, 0.03, 0.04, 0.05]
parmB = "kIPR"
valsB = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
#parmA = "IPRdf"
#valsA = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
#parmB = "IPRdn"
#valsB = [0.4]

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

print "Cell Simulation:", model, mesh

# create the top level results directory
csdir = os.getcwd()

if not os.path.exists("results"):
    os.makedirs("results")
path = "results/CS" + time.strftime("%y%m%d%H%M%S")
os.mkdir(path)
os.chdir(path)

# iterate through the parameters

for v1 in valsA:
  for v2 in valsB:
    pdir = ""
    for pv in parms:
      pdir += pv[0] + '-' + str(pv[1]) + '_'
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
        NP_MAX = 10

        # wait if at maximum number of parallel processes
        while int(os.popen("ps | grep " + model + " | wc -l").read()) >= NP_MAX:
            time.sleep(1)

        # run a non-blocking simulation process
        print(pdir)
        os.system("bash " + csdir + "/linux.sh " + model + " " + mesh + " &")
        time.sleep(5) # wait until after startup memory useage peak
    elif platform == "pan":
        print "pan"
    else:
        print "ERROR: platform not specified"    

    os.chdir("..")

# go back to top level
os.chdir(csdir)


