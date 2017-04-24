# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:04:06 2017

@author: gabriel
"""
import csv
import pandas as pd
import datetime

fullPathFilename = '/media/gabriel/UNTITLED/10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_test.csv'
#csvfile= open(fullPathFilename, 'rb')
count_id=0

df = pd.read_csv(fullPathFilename,nrows=100,skiprows=24,header=None)

df2 = pd.DataFrame()
for i in range(df.shape[0]):
    if df.iloc[i][2]=='event':
        count_id+=1
    else:
        dict1 = df.iloc[i].copy()
        dict1['ParticleId']=count_id
        df2 = df2.append(dict1,ignore_index=True)
        