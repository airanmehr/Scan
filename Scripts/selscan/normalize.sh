#!/usr/bin/env bash
norm=/home/arya/workspace/bio/Scan/selscan/bin/linux/norm
path=/home/arya/HA_selection2/Kyrgyz/hg19/phased/selscan
cd $path
for f in $(ls *.xpehh.out);do
grep -v 'nan' $f > tmp && mv tmp $f && $norm --xpehh --files $f
done

for f in $(ls *.ihs.out);do
grep -v 'nan' $f > tmp && mv tmp $f && $norm --ihs --files $f
done

for f in $(ls *.nsl.out);do
grep -v 'nan' $f > tmp && mv tmp $f && $norm --ihs --files $f
done

