# CellSims
Cell simulation runtime environment.

See README.txt for enduser runtime instructions.

##initial setup
1. (pan only) Connect to cluster from terminal:
  1. ssh -Y UPI@login.uoa.nesi.org.nz
  2. ssh -Y build-sb
2. Navigate to YOUR working directory: e.g. /projects/nesi00119/sims/JWR_CellSims
3. git clone https://github.com/jrugis/CellSims.git
4. copy and rename sweep parameters script: cp CellSims/sweep.py CellSims/_my_sweep.py
5. copy and rename executable(s): e.g. cp CellSims/executables/generic3d_03_pan CellSims/executables/generic3d_03
