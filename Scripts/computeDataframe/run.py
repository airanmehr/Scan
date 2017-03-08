'''
Copyleft Mar 07, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
import sys
sys.path.insert( 1, '/home/arya/workspace/bio/')
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;
import Utils.Util as utl
from time import  time
startTime=time()
path=utl.dataPath1000GP+'dataframe/'
utl.mkdir(path)
CHROM=sys.argv[1]
utl.VCF.computeFreqsChromosome(CHROM).to_pickle('{}chr{}.df'.format(path,CHROM))

print 'CHROM {} done in {} mins!'.format(CHROM,int((time.time()-startTime)/60))