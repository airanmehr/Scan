#!/usr/bin/env bash
chr=19
bcf=~/bin/bcftools/bcftools
cd ~/HA_selection2/1000GP/hg19/download/
ref=~/HA_selection2/hg/GRCh37/Homo_sapiens.GRCh37.dna.chromosome.$chr.fa
out=../ALL/chr$chr.vcf.gz
for i in $(ls *chr$chr.*z)
do
#    $bcf norm -m+ -c s  -f $ref $i  | $bcf filter -i "N_ALT=1 & TYPE='snp' & MAF>0"  -Oz -o $out
#    $tabix -p vcf $out
    echo $i $out
#    n0=$(zgrep -v "#" $i | wc -l) && nf=$(zgrep -v "#" $out | wc -l) && nd=$(zgrep -v '#' $i | cut -f1,2 | uniq -d|wc -l )
    #echo chr$chr'->'$n0'->'$nf'dup: '$nd

#$bcf filter -i "N_ALT=1 & TYPE='snp' & MAF>0"  $i | $bcf norm -m+ -c s  -f $ref   | $bcf filter -i "N_ALT=1 & TYPE='snp' & MAF>0"  -Oz -o $out

#$bcf norm  -c s  -f $ref $i | grep -v "#" |cut -f2

$bcf view -r 19:358307-358320 $i | grep -v "#" |cut -f1-6
echo 'HHHH'
$bcf view -r 19:358307-358320 $i  |$bcf filter -i "N_ALT=1 " | grep -v "#" |cut -f1-7
#$bcf view -r 19:358300-358320 $i  | $bcf norm  -m+ -f $ref |  grep -v "#" |cut -f1-7
#$bcf view -r 19:358307-358320 $i  | $bcf norm  -c s  -f $ref | $bcf filter -i "N_ALT=1 & TYPE='snp' & MAF>0" | grep -v "#" |cut -f1-7
 #$bcf norm -m+ -c s  -f $ref $i  | grep -v "#" |cut -f1-6
done


 #zgrep -v '#' $i | cut -f1,2 | uniq -d
