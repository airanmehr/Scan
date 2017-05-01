#!/usr/bin/env bash
echo 'running...' > ./qsub.log
echo 'running...' > ./qsub.err
for CHROM in {1..22} MT X Y
do
    qsub -l nodes=1:ppn=1 -N chr$CHROM -v CHROM=$CHROM  ./qsub.sh
done