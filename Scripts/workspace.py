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

home = os.path.expanduser('~') + '/'
import Utils.Util as utl
import Utils.Estimate as est
import Utils.Plots as pplt
from multiprocessing import Pool

def loadChrom(CHROM,pop=None):
    a=pd.read_pickle(utl.dataPath1000GP+'dataframe/chr{}.df'.format(CHROM)).iloc[:10000]
    a.index=a.index.droplevel([2,3,4])
    if pop is not None:return a[pop]
    return a

pop='CEU'; n=utl.VCF.loadPanel().groupby('pop').size()[pop]
def scanChrom(chrom,method,winSize):
    data=loadChrom(22,pop)
    return utl.scanGenome(data,lambda x: est.Estimate.getEstimate(x,method='SFSelect',n=n*2),winSize=winSize)


def scanGenome(method,winSize):
    return pd.concat(Pool(20).map(lambda x: scanChrom(x,'SFSelect',1e6),range(1,23)))

wins=[50,200,500,1000]
df=pd.concat(map(lambda w: scanGenome('SFSelecet',w),wins),1)
print df
