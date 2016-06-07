#!/bin/bash
#SBATCH -J Cell_Sim
#SBATCH -A nesi00119         # Project Account
#SBATCH --time=0:19:00       # Walltime HH:MM:SS
#SBATCH --mem-per-cpu=8G     # Memory
#SBATCH --ntasks=1           # number of tasks
#SBATCH --cpus-per-task=1    # number of threads
#SBATCH --gres=gpu:1         # for cuda version only!

# output some information
echo $HOSTNAME

# load module(s)
module load intel/2015a
module load Python/2.7.9-intel-2015a
export LD_LIBRARY_PATH=/projects/nesi00119/code/JR_petsc/petsc-3.5.4/linux-intel/lib:$LD_LIBRARY_PATH

# get variables from command line
vModel=$1   # model name
vMesh=$2    # mesh name
vRoot=$3    # simulation root directory

# run the job
srun -o "$vModel.txt" "$vRoot/executables/$vModel"

# post-processing
mv cs.dat "$vModel.dat"
mv cs.msh "$vMesh.msh"

# create reduced content output files
python "$vRoot/post/cs_reduce_min-max.py" "."

