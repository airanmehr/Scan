'''
Copyleft Mar 07, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
import sys
sys.path.insert( 1, '/home/arya/workspace/bio/')
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 40;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;
import Utils.Util as utl
from time import  time
startTime=time()
path=utl.dataPath1000GP+'dataframe/'
path='/home/arya/HA_selection2/Kyrgyz/hg19/phased/dataframe/'
fin='/home/arya/HA_selection2/Kyrgyz/hg19/phased/chr{}.vcf.gz'
panel='/home/arya/HA_selection2/Kyrgyz/kyrgyz.panel'
utl.mkdir(path)
CHROM=sys.argv[1]
utl.VCF.computeFreqsChromosome(CHROM,fin=fin,panel=panel,hap=True).to_pickle('{}chr{}.df'.format(path,CHROM))
print 'CHROM {} done in {} mins!'.format(CHROM,int((time()-startTime)/60))

# CHROM=22
# pd.read_pickle('{}chr{}.df'.format(path,CHROM))