import numpy as np;

import os; import sys
home = os.path.expanduser('~');sys.path.insert(1,home+'/workspace/bio/')
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
from itertools import product
from multiprocessing import Pool
import pylab as plt;
import matplotlib as mpl
import os
import UTILS.Util as utl
outpath='/home/arya/scan/selscan/'
def mergeXP():
    a=pd.read_csv('/home/arya/workspace/bio/Scripts/LearningSelection/XPSFS/pops',header=None).iloc[:,0]
    # for x in a:
    for x in ['CEU.YRI','CHB.YRI']:
        f = 'chr{}.xpehh.'+x+'.gz'
        out = 'xpehh.{}'.format(x)
        try:
            path = '/home/arya/POP/HAT/{}/{}/'.format(x.replace('.', '+'), x.split('.')[0])
            utl.mergeResults(path=path,f=f,out=out)
        except:
            try:
                path = '/home/arya/POP/{}/'.format(x.plit('.')[0])
                utl.mergeResults(path=path, f=f, out=out)
            except:
                print 'Error in',x


# root=/home/arya/POP
# root=/home/arya/POP/HAT/$pop"+"$popxp
# root=/home/arya/POP/KGZ/$pop"+"$popxp

def onexp(args):
    method='xpehh'
    pop,  root = args
    path = '{}{}/'.format(root,pop.split('.')[0])
    out = '{}.{}'.format(pop, method)
    f = 'chr{}.' + out + '.gz'
    utl.mergeResults(path=path, f=f, out=out, outpath=outpath)

def one(args):
    pop,method=args
    path = '/home/arya/POP/{}/'.format(pop)
    out = '{}.{}'.format(pop,method)
    f = 'chr{}.' + out + '.gz'
    utl.mergeResults(path=path, f=f, out=out,outpath=outpath)
def merge():
    pops=pd.read_csv('/home/arya/selscan/pops',header=None).iloc[:,0].tolist()

    Pool(10).map(one,product( pops,['ihs','nsl']))

def mergeXP():
    # root='/home/arya/POP/';pops='HAPH.No-HAPH No-HAPH.HAPH Healthy.Sick Normo.Hyper No-HAPH.Sick Healthy.HAPH'.split()
    # Pool(10).map(onexp, product(pops,[root]))

    root = '/home/arya/POP/HAT/';pops = 'CEU.CHB CEU.YRI CHB.YRI'.split()
    Pool(10).map(onexp, map(lambda x: (x,root+x.replace('.','+')+'/'),pops))

    root = '/home/arya/POP/KGZ/';pops = 'KGZ.JPT'.split()
    Pool(10).map(onexp, map(lambda x: (x, root + x.replace('.', '+') + '/'), pops))


if __name__=='__main__':
    # merge()
    mergeXP()
    print 'Done'

