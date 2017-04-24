# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:07:25 2017

@author: gabrielfior
"""

import os
import datetime
#import pandas as pd
import sys
##########

filedir = '/Volumes/UNTITLED/beam/10minus7_4timeslong/'
filename = '10000cm_1e6_400GeV_Rb10minus7_beam_cut1_5mm_nt_B4_g.csv'
#filename = sys.argv[1]
filename = filedir+filename
t0 = datetime.datetime.now()
with open(filename) as f:
    x = f.readlines()
    
print 'elapsed: '+str(datetime.datetime.now()-t0)    
#x = x[:1000]

list_new = []
t1 = datetime.datetime.now()
count_events=0
for i in x:
    items = i.split(',')
    if i[0]!='#' and items[3]!='event':
        
        list_new.append(items+[count_events])
    elif i[0]!='#' and items[3]=='event':
        count_events+=1
    
print 'elapsed: '+str(datetime.datetime.now()-t1)

#df = pd.DataFrame.from_records(list_new)
#df.to_csv(os.getcwd()+filename[:-4]+'_proc.csv')

#Exporting without pandas
#comment
with  open(filename[:-4]+'_proc.txt', 'w') as thefile:
	for item in list_new:
  		thefile.write("%s\n" % item)