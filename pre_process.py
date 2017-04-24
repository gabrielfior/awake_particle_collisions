# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:37:05 2016

@author: gabrielfior
"""

import os
import aux_funcs_verbose as aux


dir1 = '/Users/gabrielfior/data_mpp2/divide/'
folder_to_count='/Users/gabrielfior/data_mpp2/divide/count_folder/'
list_files = os.listdir(dir1)
list_files.remove('.DS_Store')
list_files.remove('count_folder')

#get first element
#list_files=list_files[:2]

item = []
init_list=[]
rest=[]
item_list=[]
count=0
for i in list_files:

    print 'reading ...' + str(i)

    #read file until you find G4Track
    with open(dir1+i) as f:
        x = f.readlines()
    # find
    x = rest+x
    rest=[]
    for kk,ii in enumerate(x):
        if 'G4Track' in ii and 'Particle' in ii:
            init_list.append(kk)


    for z in range(len(init_list)-1):
        item1 = x[init_list[z]:init_list[z+1]]
        item_list.append(item1)
        
        aux.write_txt(count,item1,folder_to_count)
        count = count+1

    rest.append(x[init_list[-1]:])

#Store rest
aux.write_txt(count,rest,folder_to_count)
count=count+1
    #keep rest of file for next

            
#Populate items