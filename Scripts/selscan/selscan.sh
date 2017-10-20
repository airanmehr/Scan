#!/usr/bin/env bash
echo "running...">selscan.out
procPerNode=1
pops=$(cat pops)
echo $pops
wc -l pops
echo $pops >>./selscan.out && echo $pops |wc >>./selscan.out
for pop in  $pops #KGZ #Sick HAPH
do
for method in    nsl  ihs
do
for CHROM in {1..22} #X
do
    VCF=/home/arya/POP/$pop/chr$CHROM.vcf.gz
    #python createGeneticMap.py $VCF $CHROM
    #python ./selscan.py  --method $method --vcfgz $VCF --pop $pop --panel $panel --proc 1 >> ./selscan.out 2>> ./selscan.out &
    qsub -l nodes=1:ppn=$procPerNode -N $pop.$method.$CHROM -v procPerNode=$procPerNode,VCF=$VCF,method=$method,panel=$panel,pop=$pop  qsub.sh
done
done
done

