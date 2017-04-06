'''
Copyleft Apr 05, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
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
def AAhg19(Chr,path="/home/arya/HA_selection2/Kyrgyz/hg19/AA/human_ancestor_{}.fa"):
    with open(path.format(Chr)) as f:
        f.readline()
        return f.read().replace("\n","").upper()

def f(x):
    print x.name,x.size
    if not x.size: return pd.Series(None)
    try:ref=AAhg19(x.name)
    except: return pd.Series(None)
    AA = []
    for pos in x:AA += [ref[pos - 1]]
    return pd.Series(AA,index=x)
def computeAA():
    path='/home/arya/HA_selection2/Kyrgyz/hg38/merged_vcf/DataFrame/Kyrgyz_merged_all34_NoChr_filter1_rmFORMAT.snp.info.pkl'
    a=pd.read_pickle(path);a.index.names=['CHROM','POS']
    m=pd.read_pickle('/home/arya/storage/Data/Human/Kyrgyz/data/map.df').applymap(int).reset_index().drop_duplicates(subset=['CHROM',19]).set_index('CHROM')
    aa=m[19].groupby(level=0).apply(f).rename('AA');
    aa.index.names=['CHROM',19]
    aa.reset_index()[['CHROM',19]].duplicated().sum()
    m=pd.concat([m.set_index(19,append=True),aa],1).fillna('.')
    aa=pd.concat([a[['REF','ALT']],m.reset_index().rename(columns={38:'POS'}).set_index(['CHROM','POS'])['AA']],1)
    aa.to_pickle('/home/arya/HA_selection2/Kyrgyz/hg38/AA.df')
    aa.dropna()
    aa[aa['REF']!=aa['AA']].replace({'AA':{'.':None,'-':None,'N':None}}).dropna()