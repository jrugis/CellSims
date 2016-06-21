import matplotlib.pyplot as plt
import numpy as np
import os
import struct
import sys

import cs

results_dir = str(sys.argv[1])

##################################################################
# main program
##################################################################

# navigate to the results directory
path = os.getcwd()
os.chdir(results_dir)
info = results_dir.split('/')[-1] # get info from dir 

# get the simulation time scale
t_delta, t_end = cs.get_sim_time()
y = np.linspace(0.0, t_end, t_end/t_delta, endpoint=True)

# plot the calcium and ip3 simulation data
plt.rcParams['axes.color_cycle'] = ['r', 'g', 'b']
fig, plots = plt.subplots(2, sharex=True)
plots[0].set_title('calcium')
plots[0].plot(y, np.transpose(cs.get_data('cR.bin')), lw=0.5)
plots[1].set_title('ip3')
plots[1].set_ylabel("concentration (uM)")
plots[1].plot(y, np.transpose(cs.get_data('ip3R.bin')), lw=0.5)
plt.xlabel('time (s)')
fig.text(0.02, 0.96, info)

open('../temp.pdf', 'w').close()
plt.savefig('../temp.pdf')
os.rename('../temp.pdf', '../' + info + '.pdf')

plt.show()

# go back to top level
os.chdir(path)

