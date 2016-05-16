# CellSims
Cell simulation runtime environment.

##running on pan
1. (optional) Mount cluster file system: 
  login.uoa.nesi.org.nz
2. Connect to cluster from terminal:
  ssh -Y UPI@login.uoa.nesi.org.nz
  ssh -Y build-sb
3. Navigate to YOUR working directory:
/projects/nesi00119/sims
  e.g.: JWR_CellSims/CellSims
4. Simulation setup:
  a) (optional) edit model default parameter settings
       e.g.: parameters/generic3d_03.dat 
  b) edit fixed and sweep parameters in python script file:
       run_sim.py
  c) edit Walltime as required (at least ~1 minute per 500 time steps):
       run_sim.sl
5. Run the simulation:
  a) (only required once per session) 
       module load Python/2.7.9-intel-2015a 
  b) execute python script:
       python run_sim.py
  c) (optional) check job status:
       squeue -u UPI
6. View results:
  1. get new directory name(s):
       ls -la results/
       ls results/DIR_NAME
  2. display sweep results:
       python post/cs_results_R_all.py results/DIR_NAME
  3. display individual results:
       python post/cs_results_R.py results/DIR_NAME/SUB_DIR_NAME

##running on linux

##setting up pan
1. Connect to cluster from terminal:
  ssh -Y UPI@login.uoa.nesi.org.nz
  ssh -Y build-sb
2. Navigate to YOUR working directory:
/projects/nesi00119/sims
  e.g.: JWR_CellSims/
3. git clone https://github.com/jrugis/CellSims.git

##setting up linux


