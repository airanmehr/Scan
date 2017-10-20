#!/usr/bin/env bash
panel=/home/arya/POP/ALL/panel
pops=$(tail -n+2 $panel| awk '{print $2}'  | sort | uniq) && pops=$pops' '$(tail -n+2 $panel| awk '{print $3}'  | sort | uniq) && pops=$pops' ALL HAPH No-HAPH Hyper Normo Sick Healthy KGZ'
#pops='ALL HAPH No-HAPH Hyper Normo Sick Healthy KGZ'
rm -f pops
for x in  $pops
do
    echo $x >>pops
done