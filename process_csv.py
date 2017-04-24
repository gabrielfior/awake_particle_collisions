# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:06:21 2016

@author: gabrielfior
"""

import pandas as pd
import numpy as np
import os
import graphlab

filedir = '/Users/gabrielfior/data_mpp2_data/csv_files_15steps/'
fileinput = 'xaa_csvfile.csv'

list_files=os.listdir(filedir)

list_files.remove(fileinput)
list_files.sort()
sf = graphlab.SFrame.read_csv(filedir+fileinput,delimiter=',')

for i in list_files:
    new_sframe = graphlab.SFrame.read_csv(filedir+i,delimiter=',')
    print 'lines new s frame: ' + str(new_sframe.num_rows())
    sf=sf.append(new_sframe)
    print 'num sf num rows: ' + str(sf.num_rows())


#

#df['particle_name1'] = df.apply(drop_nans,axis=1)

#Investigate single particles
