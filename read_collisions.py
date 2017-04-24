# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 01:17:28 2017

@author: gabrielfior
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.mlab as mlab
from scipy.optimize import leastsq
import os

#Read file
#reading data frame

#argon_400geV_ntp.csv

#Find tracks with secondaries
def return_tracks_with_second():

    
    filename = 'test_lowE_nt_B4_g_processed.csv'
    
    df = pd.read_csv(filename,skiprows=19,header=None,
                     names=['trackId','parentId','volumeName',
                     'particleName','stepNumber','posX','posY','posZ','perp','stepLength',
                     'kineeticEnergyDiff','edepStep','kineticEnergyPostStep','processName',
                     'fCluster','particleId'])

  
    tracks_with_secs = df[(df.particleName!='proton')].particleId.unique()
    return tracks_with_secs
   
def return_positions_track(trackId):

    filename = 'test_lowE_nt_B4_g_processed.csv'
    df = pd.read_csv(filename,skiprows=19,header=None,
                     names=['trackId','parentId','volumeName',
                     'particleName','stepNumber','posX','posY','posZ','perp','stepLength',
                     'kineeticEnergyDiff','edepStep','kineticEnergyPostStep','processName',
                     'fCluster','particleId'])

    #df_steps_secs = df[(df.particleName!='proton')]
    
    #return all positions and names for particles from track 5
    steps = df[df.particleId==trackId][['posX','posY','posZ','particleName']]
    steps_e = steps[steps.particleName=='e-']
    steps_gamma = steps[steps.particleName=='gamma']
    steps_proton = steps[steps.particleName=='proton']

    return np.array(steps_e),np.array(steps_gamma),np.array(steps_proton)