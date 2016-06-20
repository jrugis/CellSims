import matplotlib.pyplot as plt
import numpy as np
import os
import sys

import cs

results_dir = str(sys.argv[1])
rdir = results_dir.split('/')[-2]    # results directory
parms_dir = str(sys.argv[2])

##################################################################
# main program
##################################################################

# navigate to the results directory
path = os.getcwd()
os.chdir(results_dir)

# plot the calcium data
rows = 7
cols = 1
plt.rcParams['axes.color_cycle'] = ['r', 'g', 'b']
fig, plots = plt.subplots(rows, cols, sharex='col', sharey='col')
fig.canvas.set_window_title(rdir) 
fig.text(0.02, 0.96, rdir + "  " + parms_dir, fontsize=10)
fig.set_size_inches(cols * 5, rows * 2)
plots[rows-1].set_xlabel("time (s)")
plots[rows-1].set_ylabel("CA+ concentration (uM)")

for i in range(rows):
  d = str(i+1) + "/" + parms_dir
  os.chdir(d)

  # get the simulation time scale
  t_delta, t_end = cs.get_sim_time()
  x = np.linspace(0.0, t_end, t_end/t_delta, endpoint=True)

  # plot the calcium concentration
  plots[i].set_title("cell0" + str(i+1), fontsize=10)
  if os.path.isfile("cR.bin"):
    plots[i].plot(x, np.transpose(cs.get_data("cR.bin")), lw=0.5)
  os.chdir('../..')

open('../../temp.pdf', 'w').close()
plt.savefig('../../temp.pdf')
os.rename('../../temp.pdf', '../' + rdir + '.pdf')
plt.show()

# go back to top level
os.chdir(path)

