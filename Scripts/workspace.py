'''
Copyleft Mar 08, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;
import sys
sys.path.insert(1,'/home/arya/workspace/bio/Scan')
sys.path.insert(1,'/home/arya/workspace/bio')
pd.options.display.max_rows = 30;
pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;

home = os.path.expanduser('~') + '/'
import Utils.Util as utl
import Utils.Estimate as est
import Utils.Plots as pplt
from multiprocessing import Pool
import Scan.Libs.Util as sutl



if __name__ == '__main__':
    sutl.scan1000GPAll()