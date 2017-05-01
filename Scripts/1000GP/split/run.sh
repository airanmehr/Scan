chr=$1
pop=$2
bcf=~/bin/bcftools/bcftools
tabix=~/bin/tabix
path=~/HA_selection2/1000GP/hg19
ref=~/HA_selection2/hg/GRCh37/Homo_sapiens.GRCh37.dna.chromosome.$chr.fa

sam=$(grep $pop $path/ALL/panel |awk '{print $1}')
sam=$(echo $sam | tr ' ' ',')
in=$path/ALL/chr$chr.vcf.gz
out=$path/POP/$pop/chr$chr.vcf.gz
$bcf view --force-samples -s $sam  $in |$bcf filter -i "N_ALT=1 & TYPE='snp' & MAF>0 " -Oz -o $out && tabix -p vcf $out
n=$(zgrep -v "#" $out | wc -l)
echo $pop $chr $n