'''
Copyleft Mar 21, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;

np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;
import multiprocessing
pd.options.display.max_rows = 40;
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

#map(lambda x: save(f='chr{}{}.{}.out{}.norm',method=x,pop=(POP,XPPOP)[x=='xpehh']),['ihs','nsl','xpehh'][-1:])
path='/home/arya/HA_selection2/1000GP/hg19/POP/'
def SAVE(d):
    POPS=None
    def load(x,path):
        method,chrom,_,_= x.name
        skp=(0,1)[method=='xpehh']
        f=lambda x: pd.read_csv(path+'/'+x,skiprows=skp,sep='\t',header=None).iloc[:,[1,-2]].set_index(1).iloc[:,0].rename(method)
        a= f(x[0])
        a.index.name='POS'
        return a

    def getMethod(x):
        if 'ihs' in x : return 'ihs'
        if 'nsl' in x : return 'nsl'
        if 'xpehh' in x : return 'xpehh'

    outpath='/home/arya/storage/Data/Human/scan/selscan/'
    getPopXP= lambda x:x.split('_')[1].split('.')[0]
    print d
    def saveFolder(d):
        a=pd.Series(utl.files(path+d))
        a=pd.DataFrame(a[a.apply(lambda x: x[-5:]=='.norm')])
        if not a.size: return
        a['method']=a[0].apply(getMethod)
        a['POP']=d; a['POPXP']='NA';I=(a.method=='xpehh');a.loc[I,'POPXP']=a.loc[I,0].apply(getPopXP)
        a['CHROM']=a[0].apply(lambda x: utl.INT(x.split('.')[0][3:]))
        a.set_index(['method','CHROM','POP','POPXP'],inplace=True)
        return a.groupby(level=[0,1,2,3]).apply(lambda x: load(x.loc[x.name],path+d)).unstack(['method','POP','POPXP']).sort_index()

    if POPS is not None:
        if d not in POPS:return
    fout=outpath+d+'.df'
    d=saveFolder(d)
    d.to_pickle(fout)
    try:
        print d
        utl.scanGenome(pd.read_pickle(fout).abs()).to_pickle(fout.replace('.df','.idf'))
    except:
        pass
def mergeidf(path='/home/arya/storage/Data/Human/scan/selscan/'):
    print 'merging idfs'
    a=pd.Series(utl.files(path))
    a=a[a.apply(lambda x: x[-4:]=='.idf')]
    a=a[a!='panel.idf']
    b=pd.concat(map(lambda x: pd.read_pickle(path+x),a.values[:]),1).sort_index(1)
    b.to_pickle(path+'panel.idf')
    b.isnull().mean().sort_values()

# multiprocessing.Pool(10).map(SAVE,os.listdir(path) );mergeidf()
# multiprocessing.Pool(10).map(SAVE,['KGZ','Healthy','Sick','Normo','Hyper','No-HAPH','HAPH'])
# mergeidf()

def saveXPEHH(pop,popxp):
    print pop,popxp
    f=utl.home+'POP/{1}/chr{0}.{1}_{2}.xpehh.out.norm'
    a=pd.concat(map(lambda x: pd.concat([pd.read_csv(f.format(x, pop, popxp), sep='\t')[['pos', 'normxpehh']].set_index('pos').iloc[:, 0].rename(
        'xpehh')], keys=[x]),range(1,23)))
    a.index.names=['CHROM','POS']
    a.sort_index().to_pickle(utl.home+'POP/{0}/{0}.{1}.xpehh.df'.format(pop,popxp))

def SAVEXPEHH():
    # saveXPEHH('KGZ','JPT')
    # saveXPEHH('No-HAPH', 'HAPH')
    # saveXPEHH('Healthy', 'HAPH')
    # saveXPEHH('Healthy', 'Sick')
# SAVEXPEHH()


