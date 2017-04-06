'''
Copyleft Mar 21, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
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
path='/media/arya/d4565cf2-d44a-4b67-bf97-226a486c01681/Data/Human/20130502/scan/selscan/'
path='/home/arya/HA_selection2/Kyrgyz/hg19/phased/selscan/'
import Utils.Util as utl

columns={'ihs':['x','ihs1','ihs0','iHS'],'nsl':['x','sl1','sl0','nSL'],'xpehh':['gmap','x1','ihh1','x2','ihh2','xpehh']}

POP=['ALL','HAPH','No-HAPH','Normo','Hyper','Sick','Healthy']
XPPOP=['Hyper_Normo','HAPH_Healthy','HAPH_No-HAPH','No-HAPH_Sick','Sick_Healthy']
CHROM=range(1,23)
def save(f='chr{}.1kg.phase3.v5a.{}.{}.out',method='ihs',pop='CEU',savepkl=True):
    if isinstance(pop,list):
        a=pd.concat(map(lambda x: save(f=f,method=method,pop=x,savepkl=False),pop),1)
        if savepkl:a.to_pickle('{}{}.df'.format(path,method))
        return a
    else:
        print pop,method
        skp=(0,1)[method=='xpehh']
        a=pd.concat(map(lambda x: pd.read_csv(path+f.format(x,('.'+pop,'')[pop=='ALL'],method),skiprows=skp,sep='\t',header=None).iloc[:,1:].set_index(1),CHROM),keys=CHROM)
        a.index.names=['CHROM','POS']
        a.columns=columns[method]
        a=pd.concat([a],1,keys=[pop])
        a.columns.names=['POP','STAT']
        if savepkl:a.to_pickle('{}{}.{}.df'.format(path,pop,method))
        return a

def xmap(method):
    print method
    a=pd.read_pickle(path+'{}.df'.format(method))
    m=pd.read_pickle('/home/arya/storage/Data/Human/Kyrgyz/data/map.df').applymap(int).reset_index().drop_duplicates(subset=['CHROM',19]).set_index('CHROM')
    m=m.rename(columns={19:'POS'}).set_index('POS',append=True)[38]
    names=a.columns.names
    a=a.join(m,how='inner').reset_index(level='POS', drop=True).rename(columns={38:'POS'}).set_index('POS',append=True)
    a.columns=pd.MultiIndex.from_tuples(a.columns,names=names)
    a.to_pickle(path+'{}.hg38.df'.format(method))


# save(f='chr{}{}.{}.out',method='ihs',pop=POP)
# save(f='chr{}{}.{}.out',method='nsl',pop=POP)
# save(f='chr{}{}.{}.out',method='xpehh',pop=XPPOP)

xmap('ihs')
xmap('nsl')
xmap('xpehh')
