#!/usr/bin/env bash
#!/bin/bash

#PBS -m ae

#PBS -l walltime=200:00:00

#PBS -V
#PBS -e ~/qsub.out
#PBS -o ~/qsub.out
#PBS -l mem=30gb
#PBS -j oe
#PBS -p 100
cd "$PBS_O_WORKDIR"
numproc=$procPerNode
#echo $method $VCF >>~/qsub.out
python ./selscan.py   --vcfgz $VCF --vcfgzXP $VCFXP --pop $pop --popxp $popxp --panel $panel --method=xpehh --proc $numproc >> ./XPehh.out 2>> ./XPehh.out