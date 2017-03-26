#!/usr/bin/env bash
path=/pedigree2/projects/HA_selection2/Beagle/
bcf=~/bin/bcftools/bcftools
cd $path
files=$(ls *.vcf.gz)
mkdir -p filtered
cd filtered
for f in $files
do
    echo $f
    ($bcf filter -i "N_ALT=1 & TYPE='snp'" $path/$f | $bcf norm -m+ | $bcf filter -i "N_ALT=1 & TYPE='snp'" -O z -o $f &&  tabix -p vcf $f &)
done