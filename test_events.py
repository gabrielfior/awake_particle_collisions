# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 10:38:17 2016

@author: gabrielfior
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mu, sigma = 0, 0.2 # mean and standard deviation
sx = np.random.normal(mu, sigma, int(1e6))
sy = np.random.normal(mu, sigma, int(1e6))

str1 = ['# Macro file for example B4',
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
    str2 = ['/gun/position ' + '{0:.5f}'.format(sx[i]) + ' ' + '{0:.5f}'.format(sy[i]) + ' -6.0 mm',
            '/run/beamOn 1']
    for j in str2:
        str1.append(j)


with open('/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/script_pos.out','w') as outfile:
    for z in str1:
        outfile.write(z+'\n')