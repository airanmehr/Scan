'''
Copyleft Apr 17, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import sys
sys.path.insert(1,'/home/arya/workspace/bio')

import numpy as np;

np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import UTILS.Util as utl
import os,sys
import UTILS.Estimate as est
home = os.path.expanduser('~') + '/'
#CHROM=22
CHROM=sys.argv[1]
if __name__ =='__main__':
    print sys.argv
    utl.scanXPSFS(sys.argv[1].split('.'),utl.INT(sys.argv[2]))