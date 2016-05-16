To run a parameter sweep simulation, either under linux or on the pan cluster:

1) (optional, pan cluster only) Mount cluster file system: 

   login.uoa.nesi.org.nz

2) (pan only) Connect to cluster from terminal:

   ssh -Y UPI@login.uoa.nesi.org.nz
   ssh -Y build-sb

3) Navigate to YOUR working directory: 

   e.g. /projects/nesi00119/sims/JWR_CellSims/CellSims

4) Simulation setup:

   (optional) edit model default parameter settings: 
     e.g. parameters/generic3d_03.dat 

   (one time only) make a copy of the parameters script file:
     cp sweep.py _my_sweep.py
 
   edit platform, fixed and swept parameters in script file: 
     _my_sweep.py

   (pan only) edit Walltime as required (at least ~1 minute per 400 time steps):
     run_sim.sl

5) Run the simulation:

  (pan only, required once per session) 
     module load Python/2.7.9-intel-2015a 

  execute python script: 
     python run_sim.py

  (pan only, optional) check job status: 
     squeue -u UPI

6) View results:

  get new directory name(s):
    ls -la results/
    ls results/DIR_NAME

  display sweep results: 
    python post/cs_results_R_all.py results/DIR_NAME

  display individual results:
    python post/cs_results_R.py results/DIR_NAME/SUB_DIR_NAME


