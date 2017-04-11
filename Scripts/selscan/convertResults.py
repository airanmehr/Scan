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
import Scripts.KyrgysHAPH.Util as kutl
path='/media/arya/d4565cf2-d44a-4b67-bf97-226a486c01681/Data/Human/20130502/scan/selscan/'
path='/home/arya/HA_selection2/Kyrgyz/hg19/phased/selscan/'
import Utils.Util as utl
POP=['ALL','HAPH','No-HAPH','Normo','Hyper','Sick','Healthy']
XPPOP=['No-HAPH_HAPH','Healthy_HAPH','Healthy_Sick','No-HAPH_Sick','Normo_Hyper']
CHROM=range(1,23)
def save(f='chr{}.1kg.phase3.v5a.{}.{}.out',method='ihs',pop='CEU',savepkl=True):
    if isinstance(pop,list):
        fout='{}{}.df'.format(path,method)
        pd.concat(map(lambda x: save(f=f,method=method,pop=x,savepkl=False),pop),1).to_pickle(fout)
        kutl.Data.xmapTo38(fout)
        os.system( 'cp {}{}.hg38.df ~/storage/Data/Human/Kyrgyz/scan/'.format(path,method),shell=True)
    else:
        print pop,method
        skp=(0,1)[method=='xpehh']
        suff=('.100bins','')[skp]
        a=pd.DataFrame(pd.concat(map(lambda x: pd.read_csv(path+f.format(x,('.'+pop,'')[pop=='ALL'],method,suff),skiprows=skp,sep='\t',header=None).iloc[:,[1,-2]].set_index(1),CHROM),keys=CHROM).iloc[:,0].rename(method))
        a.index.names=['CHROM','POS'];a=pd.concat([a],1,keys=[pop]);a.columns.names=['POP','STAT']
        if savepkl:a.to_pickle('{}{}.{}.df'.format(path,pop,method))
        return a

map(lambda x: save(f='chr{}{}.{}.out{}.norm',method=x,pop=(POP,XPPOP)[x=='xpehh']),['ihs','nsl','xpehh'][-1:])