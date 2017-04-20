#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
panel=/home/arya/HA_selection2/Beagle/panel
path=/home/arya/HA_selection2/Beagle/filtered
#panel=~/HA_selection2/Kyrgyz/kyrgyz.panel
#for pop in HAPH No-HAPH Hyper Normo Sick Healthy ALL;do
bcf=~/bin/bcftools/bcftools
for pop in SAS AFR EAS AMR EUR
do
samples=$path/$pop.samples
grep $pop $panel | cut -f1 > $samples

for CHROM in {1..22} X
do
    echo $pop $CHROM >> ~/qsub.out
    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM
    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a
    qsub -l nodes=1:ppn=1 -N $CHROM.$pop -v pop=$pop,VCF=$VCF,samples=$samples  qsubSplit.sh
done
done

