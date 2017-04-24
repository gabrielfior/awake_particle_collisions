# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:46:33 2016

@author: gabrielfior
"""
import numpy as np
import json
import os


#filename = '/Users/gabrielfior/data_mpp2/Rb_10GeV_normal_density_Monolayer/EXYZ.txt' 
filename = '/Users/gabrielfior/data_mpp2/Rb_300MeV/EXYZ.txt' 
#/datampp2/Rb_300MeV/EXYZ

with open(filename) as f:
    x = f.readlines()

list1=[]
dict1={}
num_ions = 20

for j in range(1001):
    dict1[j] = []
    
for i in x:

    try:
        a = int(i.split(' ')[0])
        list1.append([i])
        dict1[a].append(i)
     
    except TypeError:
        print 'Error - check line '+ i
        print '\n'
        pass

    except ValueError:
        print 'Error - check line '+ i
        print '\n'
        pass
    
    
    
with open(os.getcwd()+'/exyz_dict_100.txt','w') as txt1:
    json.dump(dict1,txt1,indent=4,sort_keys=True)

