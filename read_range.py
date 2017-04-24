# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:22:21 2016

@author: gabrielfior
"""

import graphlab
import numpy as np
import matplotlib.pyplot as plt
from math import pow
import os
import pandas as pd

loading=True
full_csv_path = '/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/test_range.csv'
#Master Thesis/Share_Ubuntu/test_range.csv


columns1 =  ['currentStepNumber','energyDepositStep','r',
'perp',
'particleName',
'trackId',
'parentId',
'kineticEnergyDiff',
'stepLength',
'posX',
'posY',
'posZ',
'touchedVolume',
'processName',
'preKineticEnergy',
'postKineticEnergy',
'endStep']

#sf = graphlab.SFrame.read_csv(full_csv_path,skiprows=42,usecols=columns)
df = pd.read_csv(full_csv_path,skiprows=42,header=None)
df.columns = columns1