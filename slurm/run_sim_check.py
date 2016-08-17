
"""
Check the simulations finished successfully and restart ones that didn't.

"""
from __future__ import print_function
import os
import sys
import shutil


# get current directory
slurmdir = os.getcwd()

# loop over the list of jobs and check they worked
with open("_pan_array.in") as fh:
    count = 0
    for line in fh:
        # job details
        array = line.split()
        jobdir = array[0]
        mesh = array[3]
        model = array[2]
        csdir = array[4]
        jobargs = " ".join(array[1:])

        # switch to job directory and check it worked
        os.chdir(jobdir)
        try:
            if not os.path.exists("cR.bin"):
                # job failed
                print("Job failed in: {0}".format(jobdir))

                # copy mesh and parameter files
                if not os.path.exists("cs.dat"):
                    shutil.copy(model + ".dat", "cs.dat")
                if not os.path.exists("cs.msh"):
                    shutil.copy(mesh + ".msh", "cs.msh")

                # resubmit
                print("  Running: sbatch {0} {1}".format(os.path.join(slurmdir, "_run_sim_single.sl"), jobargs))
                os.system("sbatch {0} {1}".format(os.path.join(slurmdir, "_run_sim_single.sl"), jobargs))

                count += 1

        finally:
            os.chdir(slurmdir)

# output
print("{0} jobs failed".format(count))
