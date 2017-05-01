chr=$1
bcf=~/bin/bcftools/bcftools
tabix=~/bin/tabix
cd ~/HA_selection2/1000GP/hg19/download/
mkdir -p ../ALL
ref=~/HA_selection2/hg/GRCh37/Homo_sapiens.GRCh37.dna.chromosome.$chr.fa
out=../ALL/chr$chr.vcf.gz
for i in $(ls *chr$chr.*z)
do
    $bcf filter -i "TYPE='snp'" $i | $bcf norm -c s -f $ref -Oz -o $out.norm
    $bcf norm -m+ $out.norm | $bcf filter -i "N_ALT=1" -Oz -o $out
    rm $out.norm
    $tabix -p vcf $out
    n0=$(zgrep -v "#" $i | wc -l) && nf=$(zgrep -v "#" $out | wc -l) && nd=$(zgrep -v '#' $out | cut -f1,2 | uniq -d|wc -l ) && ndi=$(zgrep -v '#' $i | cut -f1,2 | uniq -d|wc -l )
    echo chr$chr'->'$n0'->'$nf' dup:'$ndi'->'$nd
    echo '************************************************************************************'
done