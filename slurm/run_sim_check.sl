#!/bin/bash
#SBATCH -J Cell_Sim_Check
#SBATCH -A nesi00119         # Project Account
#SBATCH --time=0:09:00       # Walltime HH:MM:SS
#SBATCH --mem-per-cpu=1G     # Memory
#SBATCH --ntasks=1           # number of tasks
#SBATCH --cpus-per-task=1    # number of threads
#SBATCH --output=check.out   # output file

# load module(s)
module load Python/2.7.9-intel-2015a

# run the job
srun python "$1/slurm/run_sim_check.py"
