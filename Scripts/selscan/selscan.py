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
import UTILS.Util as utl
chrom=22
reload(utl)
from subprocess import Popen, PIPE, STDOUT
bcf='/home/arya/bin/bcftools/bcftools'
selscan = "/home/arya/workspace/bio/Scan/selscan/bin/linux/selscan"
selscanNorm='/home/arya/workspace/bio/Scan/selscan/bin/linux/norm'
import optparse
parser = optparse.OptionParser()
parser.add_option( '--method', action="store", dest="method", help="path to synchronized file created by popoolation2")
parser.add_option( '--vcfgz', action="store", dest="vcf", help="path to pandas dataframe")
parser.add_option( '--vcfgzXP', action="store", dest="vcfXP", help="path to pandas dataframe",  default=None)
parser.add_option( '--pop', action="store", dest="pop",  default=None)
parser.add_option( '--popxp', action="store", dest="popxp",  default=None)
parser.add_option( '--panel', action="store", dest="panel", default=None)
parser.add_option( '--proc', action="store", dest="proc", default=1)
options, args = parser.parse_args()

def getCHROM(VCFin):
    return utl.INT(Popen(['zgrep -v "#" -m1 {} | cut -f1'.format(VCFin)], stdout=PIPE, stdin=PIPE, stderr=STDOUT,shell=True).communicate()[0].strip().split('\n')[-1])


def scan(VCFin, method, pop=None,panel=None,nProc=1):
    print "running {} on".format(method)#, VCFin
    chrom=getCHROM(VCFin)
    if pop is not None and '/POP/' not in VCFin:VCFin=utl.VCF.subset(VCFin,pop,panel,chrom)
    print chrom;sys.stdout.flush()
    # utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --{} --vcf {} --maf 0.1 --map {} --out {} --threads {} --trunc-ok".format(selscan,method.lower(), VCFin, VCFin+'.map', output, nProc)
    print cmd
    # os.system(cmd)
    print 'Done!',pop,chrom
    return '{}.{}.out'.format(output,method)


def split():
    panel='~/HA_selection2/Kyrgyz/kyrgyz.panel'
    for chrom in range(1,23):
        VCF='/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr{}.vcf.gz'.format(chrom)
        print chrom,VCF
        POPS=['HAPH','No-HAPH','Hyper','Normo','Healthy','Sick','ALL']
        VCF=map(lambda pop:utl.VCF.subset(VCF,pop,panel,chrom),POPS)
        map(lambda vcf:utl.VCF.createGeneticMap(vcf, chrom),VCF)

def scanXP(VCFin, VCFinXP,  pop, popXP,panel,nProc=1):
    print """
    :param VCFin: {}
    :param VCFinXP: {}
    :param pop: {}
    :param popXP: {}
    :param panel: {}
    :param nProc: {}
    """.format(VCFin, VCFinXP,  pop, popXP,panel,nProc)
    print "running {} on".format(method)#, VCFin
    chrom=getCHROM(VCFin)
    #if VCFin is None:VCFin=utl.VCF.subset(VCFin,pop,panel,chrom);#
    #if VCFinXP is None: VCFinXP=utl.VCF.subset(VCFin,popXP,panel,chrom);
    # utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --xpehh --vcf {} --vcf-ref {} --maf 0.1 --cutoff 0.1 --map {} --out {}.{}.{} --threads {} --trunc-ok".format(selscan, VCFin,VCFinXP, VCFin+'.map', output,pop,popXP, nProc)
    print cmd
    sys.stdout.flush()
    # os.system(cmd)
    print 'Done!',pop,popXP,chrom
    return '{}.{}.{}.{}.out'.format(output,pop,popXP,'xpehh')

def load(f):
    CHROM=utl.INT(f.split('chr')[1].split('.')[0])
    def one(f,CHROM,skiprows=0):
        print f
        a=pd.concat( [pd.read_csv(f,sep='\t',header=None,skiprows=skiprows).iloc[:,[1,-2]].set_index(1)],keys=[CHROM]).iloc[:,0]
        a.index.names=['CHROM','POS']
        return a
    try:a=one(f.replace('.out','.out.100bins.norm'),CHROM,0)
    except:a=one(f,CHROM,1)
    return a

if __name__ == "__main__":
    VCF,VCFXP,method,pop,panel,proc, popxp=options.vcf,options.vcfXP,options.method,options.pop,options.panel,options.proc, options.popxp
    # proc=10;VCF='/pedigree2/projects/HA_selection2/Beagle/filtered/chr2.1kg.phase3.v5a.vcf.gz';method='ihs';pop='CEU';panel='/home/arya/HA_selection2/Beagle/panel'
    #proc=10;VCF='/pedigree2/projects/HA_selection2/1000GP/hg19/POP/CEU/chr22.vcf.gz';method='ihs';pop=None;panel='/home/arya/HA_selection2/Beagle/panel'
    #proc=10;VCF='/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr22.vcf.gz';method='ihs';pop='Sick';popxp='Healthy';panel='~/HA_selection2/Kyrgyz/kyrgyz.panel'
    #proc=1;VCF='VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/KGZ/phased/HAPH/chr22.vcf.gz';pop='HAPH';method='nsl'; popxp=None;panel='~/HA_selection2/Kyrgyz/panel/kyrgyz.panel'
    #split()
    if popxp is not None or VCFXP is not None:
        out=scanXP(VCF,VCFXP,pop,popxp,panel,proc)
    else:
        out=scan(VCF,method,pop,panel,proc)
    print 'Normalizing...',out
    # os.system("grep -v 'nan' {0} > {0}.tmp && mv {0}.tmp {0} && {1} --{2} --files {0}".format(out,selscanNorm,method.replace('nsl','ihs')))
    # for x in $(ls * out); do grep -v 'nan' $x > $x.tmp & & mv $x.tmp $x & & ~ / workspace / bio / Scan / selscan / bin / linux / norm --xpehh --files $x; done
    pops = (pop, '{}.{}'.format(pop, popxp))[method == 'xpehh']
    f=os.path.dirname(out) + '/chr{}.{}.{}.gz'.format(utl.INT(out.split('chr')[1].split('.')[0]),pops,method)
    utl.gz.save(load(out).rename(method),f)

