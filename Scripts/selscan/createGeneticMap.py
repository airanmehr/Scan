'''
Copyleft May 01, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
import sys
sys.path.insert(1,'/home/arya/workspace/bio/')
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;

pd.options.display.max_rows = 20;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;

home = os.path.expanduser('~') + '/'
import Utils.Util as utl

if __name__ == "__main__":
    vcf,chrom=sys.argv[1:]
    print chrom,vcf
    utl.VCF.createGeneticMap(vcf,utl.INT(chrom),recompute=True)