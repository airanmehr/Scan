'''
Copyleft Mar 08, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
import sys
sys.path.insert(1,'/home/arya/workspace/bio/')
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
from subprocess import Popen, PIPE, STDOUT

def getCHROM(VCFin):
    return utl.INT(Popen(['zgrep -v "#" -m1 {} | cut -f1'.format(VCFin)], stdout=PIPE, stdin=PIPE, stderr=STDOUT,shell=True).communicate()[0].strip().split('\n')[-1])


def scan(VCFin, method, nProc=4):
    print "running {} on".format(method), VCFin
    selscan = "/home/arya/workspace/bio/Scan/selscan/bin/linux/selscan"
    chrom=getCHROM(VCFin)
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --{} --vcf {} --map {} --out {} --threads {} --trunc-ok".format(selscan,method.lower(), VCFin, VCFin+'.map', output, nProc)
    print cmd
    os.system(cmd)

if __name__ == "__main__":
    method,VCF=sys.argv[1],sys.argv[2]
    scan(VCF,method)
    print 'Done!'