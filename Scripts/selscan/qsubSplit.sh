#!/usr/bin/env bash
#!/bin/bash

#PBS -m ae

#PBS -l walltime=200:00:00

#PBS -V
#PBS -e ~/qsub.out
#PBS -o ~/qsub.out
#PBS -l mem=30gb
#PBS -j oe
#PBS -p 100
cd "$PBS_O_WORKDIR"
numproc=$procPerNode
bcf=~/bin/bcftools/bcftools
($bcf view $VCF.vcf.gz -S $samples -O z -o $VCF.$pop.vcf.gz && $bcf index -t $VCF.$pop.vcf.gz )>> ~/qsub.out 2>> ~/qsub.out