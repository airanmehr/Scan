#!/usr/bin/env bash
echo 'running...' > ./log
procPerNode=8
pops=$(cat pops)
for pop in $pops
do
    qsub -l nodes=1:ppn=$procPerNode -N $pop -v pop=$pop,procPerNode=$procPerNode  ./qsub.sh
done