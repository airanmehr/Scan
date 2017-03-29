#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=4
method=nsl
panel=/home/arya/HA_selection2/Beagle/panel && pop=CEU
panel=~/HA_selection2/Kyrgyz/kyrgyz.panel && pop=ALL


for method in ihs nsl
do
for CHROM in {1..22}
do
    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.vcf.gz
#    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    qsub -l nodes=1:ppn=$procPerNode -N chr$CHROM -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop  qsub.sh
done
done