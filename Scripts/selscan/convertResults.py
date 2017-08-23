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
POP=['KGZ','HAPH','No-HAPH','Normo','Hyper','Sick','Healthy']
XPPOP=['No-HAPH_HAPH','Healthy_Sick','Normo_Hyper']
CHROM=range(1,23)
def save(f='chr{}.1kg.phase3.v5a.{}.{}.out',method='ihs',POP='CEU',savepkl=True):
    print POP
    for pop in POP:
        print pop,method
        path = '/home/arya/HA_selection2/1000GP/hg19/POP/{}/'.format(pop.split('_')[0])
        skp=(0,1)[method=='xpehh']
        suff=('.100bins','')[skp]
        a=pd.DataFrame(pd.concat(map(lambda x: pd.read_csv(path+f.format(x,('','.'+pop,)['_'in pop],method,suff),skiprows=skp,sep='\t',header=None).iloc[:,[1,-2]].set_index(1),CHROM),keys=CHROM).iloc[:,0].rename(method))
        a.index.names=['CHROM','POS'];a=pd.concat([a],1,keys=[pop]);a.columns.names=['POP','STAT']
        if savepkl:a.to_pickle('{}{}.{}.df'.format(path,pop,method))

map(lambda x: save(f='chr{}{}.{}.out{}.norm',method=x,POP=(POP,XPPOP)[x=='xpehh']),['ihs','nsl','xpehh'][:1])