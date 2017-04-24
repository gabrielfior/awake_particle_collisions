# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 10:38:17 2016

@author: gabrielfior
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mu, sigma = 0, 0.2 # mean and standard deviation
sx = np.random.normal(mu, sigma, int(1e5))
sy = np.random.normal(mu, sigma, int(1e5))

str1 = ['# Macro file for Hadr06.cc example',
'/control/verbose 0',
'/run/verbose 0',
'/run/initialize',
'/process/list',
'/gun/particle proton',
'/gun/energy 400 GeV',
'/analysis/setFileName run1',
'/analysis/h1/set 1  900  0. 100. eV	#Edep',
'/analysis/h1/set 2 200  -90.   90. cm	#Edep profile',
'/analysis/h1/set 3  100  0. 15. MeV	#Eflow',
'/analysis/h1/set 4  100  0. 15. MeV	#gamma',
'/analysis/h1/set 6  200  0.001 20.  MeV log10 #neutrons',
'/analysis/h1/set 9  100  0. 15.	 MeV	#alphas',
'/analysis/h1/set 10  100  0. 15. MeV	#generic ions',
'/analysis/h1/set 14  2000  0.   3. mm	#generic ions',
'/analysis/h1/setAscii 14',
'/tracking/verbose 0']

str2 = ['# Macro file for example B4',
'# Can be run in batch, without graphic',
'# or interactively: Idle> /control/execute run1.mac',
'# Change the default number of workers (in multi-threading mode)',
'#/run/numberOfWorkers 4',
'# Initialize kernel',
'/run/initialize',
'#Tracking - either 0,1,2,3,4',
'/tracking/verbose 3',
'/gun/particle proton', 
'/gun/energy 400000 MeV']


for i in range(len(sx)):
    str2 = ['/gun/position ' + '{0:.5f}'.format(sx[i]) + ' ' + '{0:.5f}'.format(sy[i]) + ' -76.0 mm',
            '/run/beamOn 1']
    for j in str2:
        str1.append(j)


with open('/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/script_pos_v2.out','w') as outfile:
    for z in str1:
        outfile.write(z+'\n')