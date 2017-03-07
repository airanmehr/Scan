#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=1
for CHROM in {1..22} X Y
do
    qsub -l nodes=1:ppn=$procPerNode -N chr$CHROM -v CHROM=$CHROM  ./computeAF.sh.sh
done
