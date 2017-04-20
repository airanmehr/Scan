#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=1
for CHROM in  Y M #{1..22} X
do
    qsub -l nodes=1:ppn=$procPerNode -N chr$CHROM.df -v CHROM=$CHROM  ./qsub.sh
done