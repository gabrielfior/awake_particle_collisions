# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:45:07 2017

@author: gabriel
"""

# -*- coding: utf-8 -*-



import os
import csv
import sys
import datetime
import numpy as np
import sys    

#if sys.argv[1]!='':
fullPathFilename = sys.argv[1]
#else:
#fullPathFilename = '/media/gabriel/UNTITLED/beam/splitted/output_fileaa'

print 'Begin Python!' + str(datetime.datetime.now())
t0 = datetime.datetime.now()
#filedir= '/Volumes/UNTITLED/'
#filename = 'lenovo_.csv'
#filename='xaa'
count_id=0

#csvfile= open(filedir+filename, 'rb')
csvfile= open(fullPathFilename, 'rb')

spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

#outputfilename = filename[:-4] + '_processed.csv'
f = open(fullPathFilename[:-4]+'_processed.csv','wt')
writer = csv.writer(f)

    
list_elements=[]
count_id=0

for row in spamreader:

    list_elements=[]
    if '#' in row[0]:
        continue
    row_items = row[0].split(',')
    if 'event' in row_items:
        count_id += 1
    else:
        #print ', '.join(row)
        row_items.append(count_id)
        #list_elements=[]
                       
    #print list_elements
    writer.writerow(row_items)    
    
f.close()
csvfile.close()
    
print 'Time elapsed: '+ str(datetime.datetime.now()-t0)
print 'Python finished!'



#filename='/media/gabriel/UNTITLED/PAI_Geant4/10cm_1e6_400GeV_RbAwake10minus7_cut1_5mm_nt_B4_g.csv'
#pre_process_csv(filename)