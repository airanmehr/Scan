#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=4
panel=~/HA_selection2/Kyrgyz/kyrgyz.panel

popxp=Sick && pop=Healthy
#popxp=HAPH && pop=No-HAPH
#popxp=HAPH && pop=Healthy
#popxp=Sick && pop=No-HAPH
#popxp=Hyper && pop=Normo
for CHROM in {1..22}
do
#    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.vcf.gz
#    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
     vcf1=/home/arya/HA_selection2/1000GP/hg19/POP/$pop/chr$CHROM.vcf.gz
     vcf2=/home/arya/HA_selection2/1000GP/hg19/POP/$popxp/chr$CHROM.vcf.gz

    qsub -l nodes=1:ppn=$procPerNode -N $CHROM.$pop.$popxp -v procPerNode=$procPerNode,method=$method,pop=$pop,popxp=$popxp,vcf1=$vcf1,vcf2=$vcf2   qsubXP.sh
done

