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
path='/pedigree2/projects/HA_selection2/Kyrgyz/hg19/phased/'
import Utils.Util as utl

columns={'ihs':['x','ihs1','ihs0','iHS'],'nsl':['x','sl1','sl0','nSL']}
CHROM=range(1,23)
x=1
def save(f='chr{}.dial.{}.out',method='ihs'):
    a=pd.concat(map(lambda x: pd.read_csv(path+f.format(x,method),sep='\t',header=None).iloc[:,1:].set_index(1),CHROM),keys=CHROM)
    a.index.names=['CHROM','POS']
    a.columns=columns[method]
    a.to_pickle(path+'{}.df'.format(method))
    return a


save(method='ihs')
save(method='nsl')