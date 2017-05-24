#!/bin/bash
#SBATCH -J Cell_Sim_Check
#SBATCH -A nesi00119         # Project Account
#SBATCH --time=0:09:00       # Walltime HH:MM:SS
#SBATCH --mem-per-cpu=1G     # Memory
#SBATCH --ntasks=1           # number of tasks
#SBATCH --cpus-per-task=1    # number of threads
#SBATCH --output=check.out   # output file
#SBATCH --partition=debug

# load module(s)
module load Python/2.7.9-intel-2015a

# run the job
srun python "$1/slurm/run_sim_check.py"

# get the maximum memory usage
sacct -j $2 -o MaxRSS --units=M | grep M | sed  's/M//g' | sort -nr | head -1 > maxrss.txt

# get the maximum elapsed time (this won't work if it runs for more than a day as the format changes)
sacct -j $2 -o JobName,Elapsed | grep Cell_Sim | sed 's/Cell_Sim//g' | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 }' | sort -nr | head -1 > maxtime.txt
