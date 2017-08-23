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
selscanNorm='/home/arya/workspace/bio/Scan/selscan/bin/linux/norm'
import optparse
parser = optparse.OptionParser()
parser.add_option( '--method', action="store", dest="method", help="path to synchronized file created by popoolation2")
parser.add_option( '--vcfgz', action="store", dest="vcf", help="path to pandas dataframe")
<<<<<<< HEAD
parser.add_option( '--vcfgzxp', action="store", dest="vcfxp", help="path to pandas dataframe")
=======
parser.add_option( '--vcfgzXP', action="store", dest="vcfXP", help="path to pandas dataframe",  default=None)
>>>>>>> 2e1eb740ed10e8947f1ec254cd0e6604c1f5e39a
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
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --{} --vcf {} --maf 0.1 --map {} --out {} --threads {} --trunc-ok".format(selscan,method.lower(), VCFin, VCFin+'.map', output, nProc)
    print cmd
    os.system(cmd)
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

<<<<<<< HEAD

# pop='No-HAPH'
# popxp='HAPH'
# VCFin1='/home/arya/HA_selection2/1000GP/hg19/POP/No-HAPH/chr22.vcf.gz'
# VCFin2='/home/arya/HA_selection2/1000GP/hg19/POP/HAPH/chr22.vcf.gz'


def scanXP(VCFin1, VCFin2,  pop, popxp,nProc=1):
    method='xpehh'
    print "running {} on".format(method), pop,popxp
    chrom=getCHROM(VCFin1)
    utl.VCF.createGeneticMap(VCFin1, chrom)
    utl.VCF.createGeneticMap(VCFin2, chrom)
    output = VCFin1.split(".vcf")[0]
    cmd = "{} --xpehh --vcf {} --vcf-ref {} --map {} --out {}.{}_{} --threads {} --trunc-ok".format(selscan, VCFin1,VCFin2, VCFin1+'.map', output,pop,popxp, nProc)
    print cmd
    os.system(cmd)
    print 'Done!',pop,popxp,chrom
    return '{}.{}_{}.{}.out'.format(output,pop,popxp, method)

if __name__ == "__main__":
    VCF,VCFxp,method,pop,panel,proc, popxp=options.vcf,options.vcfxp,options.method,options.pop,options.panel,options.proc, options.popxp
=======
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
    utl.VCF.createGeneticMap(VCFin, chrom)
    output = VCFin.split(".vcf")[0]
    cmd = "{} --xpehh --vcf {} --vcf-ref {} --maf 0.1 --map {} --out {}.{}_{} --threads {} --trunc-ok".format(selscan, VCFin,VCFinXP, VCFin+'.map', output,pop,popXP, nProc)
    print cmd
    os.system(cmd)
    print 'Done!',pop,popXP,chrom
    return '{}.{}_{}.{}.out'.format(output,pop,popXP,'xpehh')

if __name__ == "__main__":
    VCF,VCFXP,method,pop,panel,proc, popxp=options.vcf,options.vcfXP,options.method,options.pop,options.panel,options.proc, options.popxp
>>>>>>> 2e1eb740ed10e8947f1ec254cd0e6604c1f5e39a
    # proc=10;VCF='/pedigree2/projects/HA_selection2/Beagle/filtered/chr2.1kg.phase3.v5a.vcf.gz';method='ihs';pop='CEU';panel='/home/arya/HA_selection2/Beagle/panel'
    #proc=10;VCF='/pedigree2/projects/HA_selection2/1000GP/hg19/POP/CEU/chr22.vcf.gz';method='ihs';pop=None;panel='/home/arya/HA_selection2/Beagle/panel'
    #proc=10;VCF='/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/chr22.vcf.gz';method='ihs';pop='Sick';popxp='Healthy';panel='~/HA_selection2/Kyrgyz/kyrgyz.panel'
    #proc=1;VCF='VCF=/pedigree2/projects/HA_selection2/1000GP/hg19/POP/KGZ/phased/HAPH/chr22.vcf.gz';pop='HAPH';method='nsl'; popxp=None;panel='~/HA_selection2/Kyrgyz/panel/kyrgyz.panel'
    #split()
<<<<<<< HEAD
    if popxp is not None:
        out=scanXP(VCF,VCFxp,pop,popxp,proc)
=======
    if popxp is not None or VCFXP is not None:
        out=scanXP(VCF,VCFXP,pop,popxp,panel,proc)
>>>>>>> 2e1eb740ed10e8947f1ec254cd0e6604c1f5e39a
    else:
        out=scan(VCF,method,pop,panel,proc)
    print 'Normalizing...',out
    os.system("grep -v 'nan' {0} > {0}.tmp && mv {0}.tmp {0} && {1} --{2} --files {0}".format(out,selscanNorm,method.replace('nsl','ihs')))