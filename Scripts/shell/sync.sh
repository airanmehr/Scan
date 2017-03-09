#!/usr/bin/env bash

rsync -arzuv  genomequery.ucsd.edu:/home/arya/storage/Data/Human/ /home/arya/storage/Data/Human/ #--delete
rsync -arzuv  /home/arya/storage/Data/Human/ genomequery.ucsd.edu:/home/arya/storage/Data/Human/ #--delete
