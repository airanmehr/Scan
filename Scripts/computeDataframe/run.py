'''
Copyleft Mar 07, 2017 Arya Iranmehr, PhD Student, Bafna Lab, UC San Diego,  Email: airanmehr@gmail.com
'''
import numpy as np;
import sys
sys.path.insert( 1, '/home/arya/workspace/bio/')
np.set_printoptions(linewidth=200, precision=5, suppress=True)
import pandas as pd;pd.options.display.max_rows = 20;pd.options.display.expand_frame_repr = False
import seaborn as sns
import pylab as plt;
import matplotlib as mpl
import os;
import Utils.Util as utl
from time import  time
startTime=time()


# path=utl.dataPath1000GP+'dataframe/'
# path='/home/arya/HA_selection2/Kyrgyz/hg19/phased/dataframe/'
# fin='/home/arya/HA_selection2/Kyrgyz/hg19/phased/chr{}.vcf.gz'
# fin='/home/arya/HA_selection2/Kyrgyz/hg38/merged_vcf/ByChr/hg38/chr{}_Kyrgyz_merged_all34_NoChr_filter1_rmFORMAT.vcf.gz'
# panel='/home/arya/HA_selection2/Kyrgyz/kyrgyz.panel'
# CHROM=sys.argv[1]
# #CHROM=22
# fin='/home/arya/HA_selection2/Beagle/filtered/chr{}.1kg.phase3.v5a.vcf.gz'.format(CHROM)
# panel=utl.dataPath1000GP+'integrated_call_samples_v3.20130502.ALL.panel'
# reload(utl)
# print utl.VCF.computeFreqsChromosome(CHROM,fin=fin,panel=panel,genotype= not True,save=True)
# print 'CHROM {} done in {} mins!'.format(CHROM,int((time()-startTime)/60))

def paternalMaternalChroms():
    CHROM='MT'
    fin='/home/arya/storage/Data/Human/20130502/ALL/ALL.chr{}.phase3_callmom-v0_4.20130502.genotypes.vcf.gz'
    a=utl.VCF.computeFreqsChromosome(CHROM,fin=fin,genotype= not True,save=not True,haploid=True).reset_index().replace('MT','M').set_index(['CHROM','POS','ID','REF','ALT'])
    a.to_pickle('/home/arya/storage/Data/Human/20130502/ALL/dataframe/chrM.df')
    CHROM='Y'
    fin='/home/arya/storage/Data/Human/20130502/ALL/ALL.chr{}.phase3_integrated_v2a.20130502.genotypes.vcf.gz'
    a=utl.VCF.computeFreqsChromosome(CHROM,fin=fin,genotype= not True,save=not True,haploid=True)
    a.to_pickle('/home/arya/storage/Data/Human/20130502/ALL/dataframe/chrY.df')

def mergeGenotypes():
    f='/home/arya/HA_selection2/Kyrgyz/hg38/merged_vcf/ByChr/hg38/chr{}_Kyrgyz_merged_all34_NoChr_filter1_rmFORMAT.gt.df'
    CHROM=['X','Y']+range(1,23)
    import Scripts.KyrgysHAPH.Util as kutl
    reload(kutl)
    map(lambda x:kutl.fixAA(pd.read_pickle(f.format(x)).reset_index(['ID','REF','ALT'],drop=True),True).to_pickle(f.format(x).replace('.df','.aa.df')),CHROM)
    g=[]
    x='Y'
    for x in  ['X','Y','M']+range(1,23):
        print x
        # a=pd.read_pickle(f.format(x).replace('.df','.aa.df')); if x=='M':continue
        a=pd.read_pickle(f.format(x))
        g+=[pd.concat([a.xs('No-HAPH',level=1,axis=1).apply(lambda x: x.value_counts(),1),a.xs('HAPH',level=1,axis=1).apply(lambda x: x.value_counts(),1)],1,keys=['No-HAPH','HAPH'])]
    pd.concat(g).fillna(0).to_pickle('/home/arya/HA_selection2/Kyrgyz/hg38/gt.contingency.df')

    aa=pd.concat([a.xs('No-HAPH',level=1,axis=1).apply(lambda x: x.value_counts(),1),a.xs('HAPH',level=1,axis=1).apply(lambda x: x.value_counts(),1)],1,keys=['No-HAPH','HAPH'])
    aaa=aa.iloc[:10].fillna(0).reset_index(['ID','REF','ALT'],drop=True)
    aaa.stack(level=0).groupby(level=[0,1]).apply(lambda x: utl.pval.x.T)
