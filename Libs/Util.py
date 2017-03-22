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
import os;
import Utils.Util as utl
import Utils.Estimate as est
import Utils.Plots as pplt
from multiprocessing import Pool

def loadChrom(CHROM,pop=None):
    a=pd.read_pickle(utl.dataPath1000GP+'dataframe/chr{}.df'.format(CHROM))
    a.index=a.index.droplevel([2,3,4])
    if pop is not None:return a[pop]
    return a


def scanChrom(args):
    CHROM,winSize,pop,n=args
    if isinstance(CHROM,str) or isinstance(CHROM,int):CHROM=loadChrom(CHROM,pop)
    return utl.scanGenome(CHROM,uf=lambda x: est.Estimate.getAllEstimatesX(x,n=n*2),winSize=winSize)


def scanGenome(winSize,genome,n,nProc=10):
    if isinstance(genome,str):
        args=map(lambda x: (x,winSize,genome,n),range(1,23))
    else:
        args=map(lambda x: (genome.loc[[x]],winSize,None,n),range(1,23))
    if nProc>1:
        return  pd.concat(Pool(nProc).map(scanChrom,args))
    else:
        return pd.concat(map(scanChrom,args))

def scan1000GP(pop,wins=[50,200,500,1000]):
    if pop=='ALL':n=2504
    else:n=utl.VCF.loadPanel().groupby('pop').size()[pop]
    df=pd.concat(map(lambda w: scanGenome(w*1000,pop,n),wins),1,keys=wins)
    df.to_pickle(utl.parentdir(utl.dataPath1000GP)+'/scan/{}.SFS.df'.format(pop))

def loadGenes(Intervals=True):
    a=pd.read_csv(utl.dataPath+'Human/WNG_1000GP_Phase3/gene_info.csv')[['chrom','pop','gene','POS_hg19']].rename(columns={'chrom':'CHROM','POS_hg19':'POS'})
    a.CHROM=a.CHROM.apply(lambda x: utl.INT(x[3:]))
    a=a.set_index('pop')
    if Intervals:
        a['start']=a.POS-2e6
        a['end']=a.POS+2e6
        a['name']=a.gene
    return a
def scan1000GPAll():
    pops=utl.VCF.loadPanel()
    pops=['ALL']+ pops['super_pop'].unique().tolist()+pops['pop'].unique().tolist()
    map(scan1000GP,pops)

def genesA():
    pop='CEU'
    genes=loadGenes().loc[pop]
    scan=pd.read_pickle(utl.parentdir(utl.dataPath1000GP)+'/scan/{}.SFS.df'.format(pop))
    scan.columns=[50,200,500,1000]



# a=scan[500].dropna().unstack('method')['FayWu']
# # I=range(1,5)+range(7,23)a=a.loc[I]
# pplt.Manhattan(a,shade=genes)
# for _,row in genes.iterrows():plt.annotate('{}'.format(row['name']), xy=(row.loc['gstart'], (a.max())), xytext=(row.loc['gstart'], 5),fontsize=22)




