'''
Copyleft Apr 19, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
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
import UTILS.Util as utl

def saveAA38():
    m=pd.read_pickle('/home/arya/storage/Data/Human/20130502/ALL/dataframe/map.df')
    CHROMS=range(1,23)+['X','Y']
    # from Scan.AA import AA;a=pd.concat(map(lambda CHROM:AA(m[19].loc[[CHROM]]),CHROMS))
    a=pd.read_pickle('/home/arya/storage/Data/Human/20130502/ALL/dataframe/AA.hg19.df')
    A38=map(lambda c: pd.DataFrame(a.loc[c]).join(m.loc[c].rename(columns={19:'POS'}).set_index('POS'),how='inner'),CHROMS)
    aa=pd.concat(A38,keys=CHROMS)
    aa.reset_index()
    aa=aa.reset_index('POS',drop=True).reset_index().rename(columns={38:'POS','index':'CHROM'}).set_index(['CHROM','POS'])
    aa.AA.to_pickle('/home/arya/storage/Data/Human/20130502/ALL/dataframe/AA.hg38.df')

def AAall():
    from Scan.AA import AA
    def AAchr(CHROM):
        print CHROM
        fin='/home/arya/storage/Data/Human/20130502/ALL/dataframe/chr{}.df'
        a=pd.read_pickle(fin.format(CHROM)).reset_index()
        aa=pd.DataFrame(AA(a.set_index('CHROM')['POS']).loc[CHROM])
        a=aa.join(a.set_index('POS'),how='inner')
        a=a[((a.AA==a.REF) | (a.AA==a.ALT))].reset_index().set_index(['CHROM','POS','ID','REF','ALT','AA'])
        I=a.index.get_level_values('AA')==a.index.get_level_values('ALT')
        a[I]=1-a[I]
        a=a.reset_index('REF',drop=True).reorder_levels([0,1,2,4,3])
        a.index.names=['CHROM','POS','ID','REF','ALT']
        a.to_pickle(fin.format(CHROM).replace('.df','.aa.df'))
    for CHROM in range(1,23)+['X','Y','M']:
        AAchr(CHROM)
AAall()