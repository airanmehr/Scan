#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=4
method=nSL
for CHROM in {1..22}
do
    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.dial.vcf.gz
    qsub -l nodes=1:ppn=$procPerNode -N chr$CHROM -v procPerNode=$procPerNode,VCF=$VCF,method=$method  qsub.sh
done
