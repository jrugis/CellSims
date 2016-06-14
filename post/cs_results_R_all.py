import matplotlib.pyplot as plt
import numpy as np
import os
import sys

import cs

results_dir = str(sys.argv[1])

##################################################################
# main program
##################################################################

# navigate to the results directory
path = os.getcwd()
os.chdir(results_dir)
rdir = results_dir.split('/')[-1]    # results directory
dirs = os.listdir('.')

# identify the sweep parameters, assumed 2D
sdir = dirs[0].split('_') # split directory
bdir = ""                 # base directory
for i in range(len(sdir) - 2): bdir += sdir[i] + '_' 

varA = sdir[-2].split('-')[0]
varB = sdir[-1].split('-')[0]
valsA = []
valsB = []
for d in dirs:
  valsA.append(float(d.split('_')[-2].split('-')[1].replace('p', '.')))
  valsB.append(float(d.split('_')[-1].split('-')[1].replace('p', '.')))
valsA = sorted(list(set(valsA)))
valsB = sorted(list(set(valsB)))

print valsA
print valsB

# plot the calcium data
cols = len(valsA)
rows = len(valsB)
plt.rcParams['axes.color_cycle'] = ['r', 'g', 'b']
fig, plots = plt.subplots(rows, cols, sharex='col', sharey='row')
fig.canvas.set_window_title(results_dir) 
fig.text(0.02, 0.96, rdir + '/' + bdir, fontsize=10)
fig.set_size_inches(cols * 3, rows * 3)
plots[rows-1, 0].set_xlabel("time (s)")
plots[rows-1, 0].set_ylabel("CA+ concentration (uM)")

for i in range(rows):
  for j in range(cols):
    d  = varA + '-' + str(valsA[j]).replace('.', 'p') + '_'
    d += varB + '-' + str(valsB[i]).replace('.', 'p')
    os.chdir(bdir + d)

    # get the simulation time scale
    t_delta, t_end = cs.get_sim_time()
    x = np.linspace(0.0, t_end, t_end/t_delta, endpoint=True)

    # plot the calcium concentration
    plots[rows-1-i, j].set_title(d, fontsize=10)
    if os.path.isfile("cR.bin"):
        plots[rows-1-i, j].plot(x, np.transpose(cs.get_data("cR.bin")), lw=0.5)
    os.chdir('..')

open('../temp.pdf', 'w').close()
plt.savefig('../temp.pdf')
os.rename('../temp.pdf', '../' + rdir + '.pdf')
plt.show()

# go back to top level
os.chdir(path)

