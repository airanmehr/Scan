#!/usr/bin/env bash
echo 'running XPEHH...' > ./XPehh.out
procPerNode=4
panel=~/HA_selection2/Kyrgyz/panel/kyrgyz.panel
method='xpehh'
xp='HAPH,No-HAPH No-HAPH,HAPH Healthy,Sick Normo,Hyper No-HAPH,Sick KGZJ,JPTK Healthy,HAPH KGZJ,JPTK'
xp='CEU,CHB YRI,CEU YRI,CHB'
root=/home/arya/POP
root=/home/arya/POP/ALL
for i in $xp; do IFS=","; set -- $i; pop=$1;popxp=$2; echo $pop $popxp;
for CHROM in {1..22}
do
#    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    VCF=$root/$pop/chr$CHROM.vcf.gz
    VCFXP=$root/$popxp/chr$CHROM.vcf.gz
#    python createGeneticMap.py $VCF $CHROM
#    python ./selscan.py   --vcfgz $VCF --vcfgzXP $VCFXP --pop $pop --popxp $popxp --panel $panel --method=xpehh --proc 1 >> ./XPehh.out 2>> ./XPehh.out &
    qsub -l nodes=1:ppn=$procPerNode -N $CHROM.$pop.$popxp -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop,popxp=$popxp,VCFXP=$VCFXP qsubXP.sh
done
done