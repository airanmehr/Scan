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
import Utils.Util as utl

columns={'ihs':['x','ihs1','ihs0','iHS'],'nsl':['x','sl1','sl0','nSL']}
CHROM=range(1,23)
x=1
def save(f='chr{}.1kg.phase3.v5a.{}.{}.out',method='ihs',pop='CEU'):
    a=pd.concat(map(lambda x: pd.read_csv(path+f.format(x,pop,method),sep='\t',header=None).iloc[:,1:].set_index(1),CHROM),keys=CHROM)
    a.index.names=['CHROM','POS']
    a.columns=columns[method]
    a.to_pickle('{}{}.{}.df'.format(path,pop,method))
    return a


save(method='ihs')
save(method='nsl')