'''
Copyleft Apr 17, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;

np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import Utils.Util as utl
import os,sys
import Utils.Estimate as est
home = os.path.expanduser('~') + '/'
#CHROM=22
CHROM=sys.argv[1]
fname='/home/arya/HA_selection2/Beagle/filtered/chr{}.1kg.phase3.v5a.aa.df'.format(CHROM)
pop=utl.VCF.loadPanel().groupby('super_pop').size()
pop
df=pd.read_pickle(fname)[pop.index]
winSize=50000
f=lambda x: pd.DataFrame(utl.scanGenome(x[x.name],uf=lambda X: est.Estimate.getEstimate(X, n=pop[x.name],  bins=20,removeFixedSites=True,normalizeTajimaD= False),winSize=winSize ))
stats=df.groupby(level=0,axis=1).apply(f).T.reset_index(level=0,drop=True).T
stats.to_pickle(fname.replace('.df','.SFS.df'))
