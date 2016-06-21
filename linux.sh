#!/bin/bash

# run the simulation
$4/executables/$1 > $1.txt

#rename the data files
mv cs.dat $2.dat
mv cs.msh $3.msh

# create reduced content output files
python $4/post/cs_reduce_min-max.py .



