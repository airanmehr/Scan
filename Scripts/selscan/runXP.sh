#!/usr/bin/env bash
echo 'running XPEHH...' > ./XPehh.out
procPerNode=4
panel=~/HA_selection2/Kyrgyz/panel/kyrgyz.panel
method='xpehh'
xp='HAPH,No-HAPH No-HAPH,HAPH Healthy,Sick Normo,Hyper No-HAPH,Sick'

<<<<<<< HEAD
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
=======
for i in $xp; do IFS=","; set -- $i; pop=$1;popxp=$2; echo $pop $popxp;
for CHROM in 15 # #{1..22}
do
#    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/$pop/chr$CHROM.vcf.gz
    VCFXP=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/$popxp/chr$CHROM.vcf.gz
    #python createGeneticMap.py $VCF $CHROM

    #python ./selscan.py   --vcfgz $VCF --vcfgzXP $VCFXP --pop $pop --popxp $popxp --panel $panel --method=xpehh --proc 1 >> ./XPehh.out 2>> ./XPehh.out &

    #qsub -l nodes=1:ppn=$procPerNode -N $CHROM.$pop.$popxp -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop,popxp=$popxp,VCFXP=$VCFXP qsubXP.sh
>>>>>>> 2e1eb740ed10e8947f1ec254cd0e6604c1f5e39a
done


done