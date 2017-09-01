#!/usr/bin/env bash
echo "running...">selscan.out
procPerNode=4
panel=/home/arya/POP/ALL/panel
#panel=~/HA_selection2/Kyrgyz/panel/kyrgyz.panel
pops=$(tail -n+2 $panel| awk '{print $2}'  | sort | uniq) && pops=$pops' '$(tail -n+2 $panel| awk '{print $3}'  | sort | uniq) && pops=$pops ' ALL HAPH No-HAPH Hyper Normo Sick Healthy KGZ'
echo $pops
echo $pops | wc
echo $pops >>./selscan.out && echo $pops |wc >>./selscan.out
for pop in  $pops #KGZ #Sick HAPH
do
for method in    nsl  ihs
do
for CHROM in {1..22} #X
do

    VCF=/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr$CHROM.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/Beagle/filtered/chr$CHROM.1kg.phase3.v5a.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/$pop/chr$CHROM.vcf.gz
    VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/$pop/chr$CHROM.vcf.gz

    #python createGeneticMap.py $VCF $CHROM
    #python ./selscan.py  --method $method --vcfgz $VCF --pop $pop --panel $panel --proc 1 >> ./selscan.out 2>> ./selscan.out &
    qsub -l nodes=1:ppn=$procPerNode -N $pop.$method.$CHROM -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop  qsub.sh
done
done
done

