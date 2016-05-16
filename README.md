# CellSims
Cell simulation runtime environment.

##running on pan
1. (optional) Mount cluster file system: login.uoa.nesi.org.nz
2. Connect to cluster from terminal:
  1. ssh -Y UPI@login.uoa.nesi.org.nz
  2. ssh -Y build-sb
3. Navigate to YOUR working directory:
  1. e.g.: /projects/nesi00119/sims/JWR_CellSims/CellSims
4. Simulation setup:
  1. (optional) edit model default parameter settings
    1.   e.g.: parameters/generic3d_03.dat 
  2. edit platform, fixed and sweep parameters in python script file: run_sim.py
  3. edit Walltime as required (at least ~1 minute per 500 time steps): run_sim.sl
5. Run the simulation:
  1. (only required once per session) module load Python/2.7.9-intel-2015a 
  2. execute python script: python run_sim.py
  3. (optional) check job status: squeue -u UPI
6. View results:
  1. get new directory name(s):
    1. ls -la results/
    2. ls results/DIR_NAME
  2. display sweep results: python post/cs_results_R_all.py results/DIR_NAME
  3. display individual results: python post/cs_results_R.py results/DIR_NAME/SUB_DIR_NAME

##running on linux

##setting up pan
1. Connect to cluster from terminal:
  1. ssh -Y UPI@login.uoa.nesi.org.nz
  2. ssh -Y build-sb
2. Navigate to YOUR working directory:
  1. e.g.: /projects/nesi00119/sims/JWR_CellSims
3. git clone https://github.com/jrugis/CellSims.git
4. copy and rename executable:
  1. e.g.: cp CellSims/executables/generic3d_03_pan CellSims/executables/generic3d_03

##setting up linux


