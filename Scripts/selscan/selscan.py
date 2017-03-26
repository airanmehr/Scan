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
parser.add_option( '--panel', action="store", dest="panel", default=None)
parser.add_option( '--proc', action="store", dest="proc", default=1)
options, args = parser.parse_args()

def getCHROM(VCFin):
    return utl.INT(Popen(['zgrep -v "#" -m1 {} | cut -f1'.format(VCFin)], stdout=PIPE, stdin=PIPE, stderr=STDOUT,shell=True).communicate()[0].strip().split('\n')[-1])


def scan(VCFin, method, pop=None,panel=None,nProc=4):
    print "running {} on".format(method)#, VCFin
    chrom=getCHROM(VCFin)
    if pop is not None:VCFin,panel=subset(VCFin,pop,panel,chrom)
    print chrom;sys.stdout.flush()
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --{} --vcf {} --map {} --out {} --threads {} --trunc-ok".format(selscan,method.lower(), VCFin, VCFin+'.map', output, nProc)
    print cmd
    os.system(cmd)
    if pop is not None:
        os.remove(VCFin);os.remove(panel)
def subset(VCFin, pop,panel,chrom):
    assert len(pop)
    print 'Creating a vcf.gz file for individuals of {} population'.format(pop)
    fileSamples='{}.{}.chr{}'.format(panel,pop,chrom)
    fileVCF=VCFin.replace('.vcf.gz','.{}.vcf.gz'.format(pop))
    os.system('grep {} {} | cut -f1 >{}'.format(pop,panel,fileSamples))
    cmd="{} view -S {} {} | {} filter -i \"N_ALT=1 & TYPE='snp'\" -O z -o {}".format(bcf,fileSamples,VCFin,bcf,fileVCF)
    os.system(cmd)
    return fileVCF,fileSamples

if __name__ == "__main__":
    VCF,method,pop,panel,proc=options.vcf,options.method,options.pop,options.panel,options.proc
    #proc=10;VCF='/pedigree2/projects/HA_selection2/Beagle/filtered/chr2.1kg.phase3.v5a.vcf.gz';method='ihs';pop='CEU';panel='/home/arya/HA_selection2/Beagle/panel'
    scan(VCF,method,pop,panel,proc)
    print 'Done!'