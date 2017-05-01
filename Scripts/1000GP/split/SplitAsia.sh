#!/usr/bin/env bash
bcf=~/bin/bcftools/bcftools
tabix=~/bin/tabix
path=~/HA_selection2/1000GP/hg19
mkdir -p $path/POP/ASIA

sam=$(grep SAS $path/ALL/panel |awk '{print $1}')' '$(grep EAS $path/ALL/panel |awk '{print $1}')
sam=$(echo $sam | tr ' ' ',')

chr=22
for chr in {11..22} X Y MT
do
in=$path/ALL/chr$chr.vcf.gz
out=$path/POP/ASIA/chr$chr.vcf.gz
($bcf view --force-samples -s $sam  $in |$bcf filter -i "N_ALT=1 & TYPE='snp'" -Oz -o $out && tabix -p vcf $out  ) &
#n=$(zgrep -v "#" $out | wc -l) &&
echo  $chr
done