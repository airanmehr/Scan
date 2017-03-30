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
bcf='/home/arya/bin/bcftools/bcftools'
selscan = "/home/arya/workspace/bio/Scan/selscan/bin/linux/selscan"

import optparse
parser = optparse.OptionParser()
parser.add_option( '--method', action="store", dest="method", help="path to synchronized file created by popoolation2")
parser.add_option( '--vcfgz', action="store", dest="vcf", help="path to pandas dataframe")
parser.add_option( '--pop', action="store", dest="pop",  default=None)
parser.add_option( '--popxp', action="store", dest="popxp",  default=None)
parser.add_option( '--panel', action="store", dest="panel", default=None)
parser.add_option( '--proc', action="store", dest="proc", default=1)
options, args = parser.parse_args()

def getCHROM(VCFin):
    return utl.INT(Popen(['zgrep -v "#" -m1 {} | cut -f1'.format(VCFin)], stdout=PIPE, stdin=PIPE, stderr=STDOUT,shell=True).communicate()[0].strip().split('\n')[-1])


def scan(VCFin, method, pop=None,panel=None,nProc=4):
    print "running {} on".format(method)#, VCFin
    chrom=getCHROM(VCFin)
    if pop is not None:VCFin=utl.VCF.subset(VCFin,pop,panel,chrom)
    print chrom;sys.stdout.flush()
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --{} --vcf {} --map {} --out {} --threads {} --trunc-ok".format(selscan,method.lower(), VCFin, VCFin+'.map', output, nProc)
    print cmd
    os.system(cmd)
    if (pop is not None) and (pop != 'ALL'):os.remove(VCFin);

def scanXP(VCFin,  pop1, pop2,panel,nProc=4):
    print "running {} on".format(method)#, VCFin
    chrom=getCHROM(VCFin)
    if pop is not None:
        VCFin1=utl.VCF.subset(VCFin,pop1,panel,chrom)
        utl.VCF.createGeneticMap(VCFin1, chrom)
    if pop is not None:
        VCFin2=utl.VCF.subset(VCFin,pop2,panel,chrom)
        utl.VCF.createGeneticMap(VCFin2, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --xpehh --vcf {} --vcf-ref {} --map {} --out {}.{}_{} --threads {} --trunc-ok".format(selscan, VCFin1,VCFin2, VCFin1+'.map', output,pop,popxp, nProc)
    print cmd
    os.system(cmd)
    if pop is not None:
        if pop is not 'ALL':os.remove(VCFin1);
    if popxp is not None:
        if popxp is not 'ALL':os.remove(VCFin2);

if __name__ == "__main__":
    VCF,method,pop,panel,proc, popxp=options.vcf,options.method,options.pop,options.panel,options.proc, options.popxp
    # proc=10;VCF='/pedigree2/projects/HA_selection2/Beagle/filtered/chr2.1kg.phase3.v5a.vcf.gz';method='ihs';pop='CEU';panel='/home/arya/HA_selection2/Beagle/panel'
    # proc=10;VCF='/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr22.vcf.gz';method='ihs';pop='Sick';popxp='Healthy';panel='~/HA_selection2/Kyrgyz/kyrgyz.panel'
    if popxp is not None:
        scanXP(VCF,pop,popxp,panel,proc)
    else:
        scan(VCF,method,pop,panel,proc)
    print 'Done!',pop,popxp