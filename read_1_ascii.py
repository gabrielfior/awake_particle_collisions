# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv(('/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run1.ascii'))

filepath1='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run0_0.ascii'
#filepath2='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run1_0,2_0.ascii'
#filepath3='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run_-0,2_0.ascii'

x2=[]
x1=[]
x3=[]
with open(filepath1) as f:
    x1.append(f.readlines())

x1 = x1[0][4:]



xbin=[]
y1=[]   
for a in x1:
    xbin.append(np.double(a.split('\t')[1]))
    y1.append(np.double(a.split('\t')[2].replace('\n','')))
    
y2=[]
xbin2=[]
#for i,j in enumerate(y1):
#    if j !=0:
#        y2.append(j)
#        xbin2.append(xbin[i])        
plt.figure(1)
plt.clf()
plt.scatter(xbin,np.log(y1))
plt.title('Energy deposition - radial distribution')
plt.xlabel('r (mm)')
plt.ylabel('Energy deposited (eV)')
#plt.xlim([0,1.0])
