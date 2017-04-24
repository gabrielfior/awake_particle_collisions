# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:07:25 2017

@author: gabrielfior
"""

import os
import datetime
import pandas as pd
import sys
import numpy as np


##########

#filename = '10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g_backup.csv'
filename = sys.argv[1]


t0 = datetime.datetime.now()
with open(filename) as f:
    x = f.readlines()
    
print 'elapsed: '+str(datetime.datetime.now()-t0)    
#x = x[:100000]

list_new = []
t1 = datetime.datetime.now()
count_events=0
for counting,i in enumerate(x):
    if counting%1000000==0:
        print counting
        
    items = i.split(',')
    if i[0]!='#' and items[3]!='event':
        
        list_new.append(items+[count_events])
    elif i[0]!='#' and items[3]=='event':
        count_events+=1
    
print 'elapsed: '+str(datetime.datetime.now()-t1)

df = pd.DataFrame.from_records(list_new)
df[19] = df[19].apply(lambda x: np.float(x[:-1]))
df.to_csv(os.getcwd()+'/'+filename[:-4]+'_proc.csv',index_label='IndexCol')
print 'done'