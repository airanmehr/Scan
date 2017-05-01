#!/usr/bin/env bash
echo 'running...' >> ./qsub.log
echo 'running...' >> ./qsub.err
path=~/HA_selection2/1000GP/hg19

cp $path/download/integrated_call_samples_v3.20130502.ALL.panel $path/ALL/panel
pops=$(tail -n+2 $path/ALL/panel| awk '{print $2}'  | sort | uniq) && pops=$pops' '$(tail -n+2 $path/ALL/panel| awk '{print $3}'  | sort | uniq)
mkdir -p $path/POP

for pop in  $pops
do
    mkdir -p $path/POP/$pop
    for chr in {1..22} X Y MT
    do
        qsub -l nodes=1:ppn=1 -N $pop.chr$chr -v CHROM=$chr,pop=$pop  qsub.sh
    done
done