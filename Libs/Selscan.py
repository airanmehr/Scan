'''
Copyleft Mar 08, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;

np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os
import Utils.Util as utl
chrom=22
reload(utl)

def iHS(VCFin, chrom, nProc=4):
    print "running iHS ..."
    selscan = "/home/arya/workspace/bio/Scan/selscan/bin/linux/selscan"
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --ihs --vcf {} --map {} --out {} --threads {} --trunc-ok".format(selscan, VCFin, VCFin+'.map', output, nProc)
    os.system(cmd)
    return output+".ihs.out"

VCFin='/media/arya/d4565cf2-d44a-4b67-bf97-226a486c01681/Data/Human/Kyrgyz/data/chr22_Kyrgyz_merged_all34_NoChr_filter1_rmFORMAT.vcf.gz'
iHS(VCFin,22)