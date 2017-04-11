#!/usr/bin/env bash
echo 'running...' > ~/qsub.out
procPerNode=4
panel=~/HA_selection2/Kyrgyz/kyrgyz.panel

popxp=HAPH && pop=No-HAPH
popxp=HAPH && pop=Healthy
popxp=Sick && pop=No-HAPH
popxp=Sick && pop=Healthy
popxp=Hyper && pop=Normo
for CHROM in {1..22}
do
    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.vcf.gz
#    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    qsub -l nodes=1:ppn=$procPerNode -N $CHROM.$pop.$popxp -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop,popxp=$popxp   qsubXP.sh
done

