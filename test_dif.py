# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:06:14 2016

@author: gabrielfior
"""
import numpy as np

file1 = '/Users/gabrielfior/data_mpp2_data/test_hioni/'
file0 = file1+"xaa"
#file1 = '/media/gabriel/6CA49654A496211E/B4-build/divide/'
with open(file0) as f:
    x = f.readlines()
    

proc_name=[]
edep=[]
kin_energy=[]
list_step_lines=[]
for i,j in enumerate(x):

    #Find line step
    if 'Step# ' in j or '#Step#' in j:
        list_step_lines.append(i)
        proc_name.append(x[i+1])
        edep.append(x[i+12])
        kin_energy.append(x[i+29])
    # Skip ??? lines
    # FInd energy deposited
    #Find pre kinetic energy
    # Find post kinetic energy


    #        list_store.append(j)
    #    list_post.append(filter(None,j.split(' '))[-1].replace('\n',''))
    #    list_pre.append(filter(None,j.split(' '))[-2].replace('\n',''))

    
