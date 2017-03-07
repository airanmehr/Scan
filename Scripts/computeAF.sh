#!/usr/bin/env bash
PYTHONPATH="${PWD%/*}"
echo $PYTHONPATH
for i in {1..22} X Y
do
    python ./computeAF.py $i
done