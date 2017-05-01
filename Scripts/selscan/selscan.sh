#!/usr/bin/env bash
#echo "running...">selscan.out
procPerNode=1
panel=/home/arya/HA_selection2/1000GP/hg19/Beagle/panel
#panel=~/HA_selection2/Kyrgyz/kyrgyz.panel
#for pop in HAPH No-HAPH Hyper Normo Sick Healthy ALL
#pops=$(tail -n+2 $panel| awk '{print $2}'  | sort | uniq) && pops=$pops' '$(tail -n+2 $panel| awk '{print $3}'  | sort | uniq)
#pops=$pops ' ALL'
pops=$(qstat | grep arya | grep "H " | awk '{print $2}' | tr '.' '\t' | cut -f1  | uniq |xargs)
echo $pops
echo $pops | wc
echo $pops >>./selscan.out && echo $pops |wc >>./selscan.out
for pop in $pops
do
for method in   ihs nsl
do
for CHROM in {1..22} X
do

    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/$pop/chr$CHROM.vcf.gz
    #python ./selscan.py   --vcfgz $VCF --pop $pop --panel $panel --method $method --proc 1
    qsub -l nodes=1:ppn=$procPerNode -N $pop.$method.$CHROM -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop  qsub.sh
done
done
done

