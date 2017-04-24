# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:20:37 2017

@author: gabrielfior
"""

import pandas as pd
import numpy as np
import datetime
from itertools import islice
import sys
import os

#filedir = '/Volumes/UNTITLED/beam/'
#filename = '10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g_proc.txt'

#filedir=sys.argv[1]
#filename=sys.argv[2]

#print 'processing: '+filedir+filename

def read_txt_export_csv(filedir,filename):
    t0=datetime.datetime.now()
    with open(filedir+filename,'r') as f:
        head = f.readlines()
    
    #N=1000
    #with open(filedir+filename,'r')as myfile:
    #    head = list(islice(myfile, N))
    
    print 'elapsed reading: '+str(datetime.datetime.now()-t0)
    
    list_new=[]
    t0=datetime.datetime.now()
    for j,i in enumerate(head):
        if j%100000 == 0:
            print 'line: ' + str(j)
            
        items = i.split(',')
        list_temp=[]
        for j in items:
            try:
                item1 = np.double(j.replace('[','').replace("'","").replace("\\n","").replace(']',''))
                list_temp.append(item1)
            except ValueError:
                item1 = j.replace('[','').replace("'","").replace('\\n','').replace("\n","").replace(']','')
                list_temp.append(item1)
        list_new.append(list_temp)    
    
    print 'elapsed converting to list: '+str(datetime.datetime.now()-t0)
    
    columns_new2 =['trackId','parentId','volumeName','particleName','stepNumber',
                                                   'posX','posY','posZ','perp','kineeticEnergyDiff',
                                                   'edepStep','kineticEnergyPostStep','processName',
                                    'mompreX','mompreY','mompreZ','momposX','momposY','momposZ',
                  'stepLength','particleId'] 
    df = pd.DataFrame.from_records(list_new,columns=columns_new2)
    df.to_csv(filedir+filename+'_proc.csv',columns=columns_new2,header=False,index=False)
print 'done'
#corrections
filedir = '/Users/gabrielfior/Dropbox/Test82-build/splitted/'
#filedir = '/home/iwsatlas1/fior/Dropbox/Test82-build/splitted/'
list_files = os.listdir(filedir)
list_files_new=[]
for j in list_files:
    #if 'cm' not in j:
    if 'join' not in j:        
        list_files_new.append(j)

for filename in list_files_new:
    print 'process: '+filename
    read_txt_export_csv(filedir,filename)
    
