import os
import sys

results_dir = str(sys.argv[1])
dirs = os.listdir(results_dir)
for d in dirs:
  print results_dir + "/" + d
  os.system("python cs_reduce_min-max.py " + results_dir + "/" + d + " &")

