To run a parameter sweep simulation, either under on a linux workstation or on the pan cluster:

1) (optional, pan cluster only) Mount cluster file system: 

   login.uoa.nesi.org.nz

2) (pan only) Connect to cluster from terminal:

   ssh -Y UPI@login.uoa.nesi.org.nz
   ssh -Y build-sb

3) Navigate to YOUR working directory: 

   e.g. /projects/nesi00119/sims/JWR_CellSims/CellSims

4) Simulation setup:

   (one time only) make a copy of the parameters script file:
     cp sweep.py _my_sweep.py
 
   edit platform, solver, model, mesh type, fixed and swept parameters in script file: 
     _my_sweep.py

   (pan only) edit Walltime (at least ~5 minutes per every 100 seconds of simulation time) and resources as required:
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
    for a given cell: 
      python post/cs_results_R_cell.py results/DIR_NAME CELL_NUMBER
    across all cells for a given parameter:
      python post/cs_results_R_parm.py results/DIR_NAME PARAMETERS

  display individual results:
    python post/cs_results_R-single.py results/DIR_NAME/SUB_DIR_NAME


