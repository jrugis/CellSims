#!/bin/bash

# run the simulation
../../../executables/$1 > $1.txt

#rename the data files
mv cs.dat $1.dat
mv cs.msh $2.msh

# create reduced content output files
python ../../../post/cs_reduce_min-max.py .



