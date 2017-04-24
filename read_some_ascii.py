# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
#df = pd.read_csv(('/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run1.ascii'))

filepath1='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/runs_new/'
#filepath2='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run1_0,2_0.ascii'
#filepath3='/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/run_-0,2_0.ascii'

x1=[]
listfiles=os.listdir(filepath1)
for i in listfiles:
    with open(filepath1+i) as f:
        x1.append(f.readlines())

y=[]
for i in x1:
    if '\n' != i and '1D histogram' not in i:   
        y+=i
   
y2=[]
for i,j in enumerate(y):
    if len(j)>=20:
        if 'histogram' not in j:
            y2.append(j)

bin1=[]
y1=[]
index=[]
new1=[]
for i in y2:
    a=i.split('\t')
    index.append(np.int(a[0]))
    bin1.append(np.double(a[1]))
    y1.append(np.double(a[2]))
    new1.append([a[0],a[1],np.double(a[2][:-1])])

df = pd.DataFrame(new1)
df.columns=['index','bin','value']


group = df.groupby('bin').sum()

xbin=np.array(group.index)
y1 = [] 

for i in group.value:
    y1.append(i)

y1=np.array(y1)



    
#y2=[]
#xbin2=[]
#for i,j in enumerate(y1):
#    if j !=0:
#        y2.append(j)
#        xbin2.append(xbin[i])        

plt.figure(1)
plt.clf()
#plt.scatter(xbin2,np.log(y2))
plt.scatter(list(xbin),y1)
plt.title('Log of energy deposition - radial distribution')
plt.xlabel('r (mm)')
plt.ylabel('log(Energy deposited (eV)) ')
#plt.xlim([0,1.0])
