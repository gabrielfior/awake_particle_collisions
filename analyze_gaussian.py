# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:36:17 2016

@author: gabrielfior
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import numpy as np

col_names=['currentStepNumber','energyDepositStep','r','perp','particleName','trackId','parentId',
           'kineticEnergyDiff', 'stepLength','posX','posY','posZ','volume','processName','preKineticEnergy',
           'postKineticEnergy','endStep','particleId']
#col_names=['currentStepNumber','energyDepositStep','r','perp','particleName','kineticEnergyDiff'
#           ,'stepLength','posX','posY','posZ','volume','from_step','particleId']
filename = '/Volumes/UNTITLED/Geant4_data/output_power7.csv'


#df = pd.read_csv(filename,header=None,names=col_names)
df = pd.read_csv(filename,header=None,names=col_names)


#df = df['particleName','particleId','trackId','parentId','currentStepNumber','posX','posY','posZ']
df.drop(['r','perp','kineticEnergyDiff','stepLength','volume','processName',
         'preKineticEnergy','postKineticEnergy','endStep' ],axis=1,inplace=True)
#df.drop(['r','perp','particleId'],axis=1)
print 'ok'

#df.posX = df.posX.fillna(value=0)
#df.posY = df.posY.fillna(value=0)

# Create radial coordinate
df['posR'] = np.sqrt(df.posX**2 + df.posY**2)
#Improve - last steps not always at border - make group by
first_steps = df[(df.currentStepNumber==1) & (df.particleName == 'proton') & (df.parentId==0)]
#last_steps  = df[(df.currentStepNumber==12) & (df.particleName == 'proton') & (df.parentId==0)]

#Everything that comes out
last_steps = df.groupby(['particleId','trackId','parentId'],as_index=False).agg({
                'currentStepNumber': np.max, 'posZ':np.max})

                                            

last_steps = last_steps[last_steps.posZ >= 50.0]  
df_proton_end = pd.merge(df, last_steps, how='right', on=['particleId','trackId','parentId','currentStepNumber'])
#s1 = pd.merge(df1, df2, how='left', on=['Year', 'Week', 'Colour'])
del (df)
df_proton_end_onlyProtons = df_proton_end[df_proton_end.particleName=='proton']

#################
#All



# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))


datax = first_steps.posX
histx, bin_edgesx = np.histogram(datax, density=True,bins=100)
bin_centresx = (bin_edgesx[:-1] + bin_edgesx[1:])/2

datay = first_steps.posY
histy, bin_edgesy = np.histogram(datay, density=True,bins=100)
bin_centresy = (bin_edgesy[:-1] + bin_edgesy[1:])/2

datax2 = df_proton_end.posX
histx2, bin_edgesx2 = np.histogram(datax2, density=True,bins=100)
bin_centresx2 = (bin_edgesx2[:-1] + bin_edgesx2[1:])/2

datay2 = df_proton_end.posY
histy2, bin_edgesy2 = np.histogram(datay2, density=True,bins=100)
bin_centresy2 = (bin_edgesy2[:-1] + bin_edgesy2[1:])/2

datax2p = df_proton_end_onlyProtons.posX
histx2p, bin_edgesx2p = np.histogram(datax2p, density=True,bins=100)
bin_centresx2p = (bin_edgesx2p[:-1] + bin_edgesx2p[1:])/2

datay2p = df_proton_end_onlyProtons.posY
histy2p, bin_edgesy2p = np.histogram(datay2p, density=True,bins=100)
bin_centresy2p = (bin_edgesy2p[:-1] + bin_edgesy2p[1:])/2


# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [1., 0., 1.]
coeffx, var_matrixx = curve_fit(gauss, bin_centresx, histx, p0=p0)
coeffy, var_matrixy = curve_fit(gauss, bin_centresy, histy, p0=p0)

coeffx2, var_matrixx2 = curve_fit(gauss, bin_centresx2, histx2, p0=p0)
coeffy2, var_matrixy2 = curve_fit(gauss, bin_centresy2, histy2, p0=p0)

coeffx2p, var_matrixx2p = curve_fit(gauss, bin_centresx2p, histx2p, p0=p0)
coeffy2p, var_matrixy2p = curve_fit(gauss, bin_centresy2p, histy2p, p0=p0)



# Get the fitted curve
hist_fitx = gauss(bin_centresx, *coeffx)
hist_fity = gauss(bin_centresy, *coeffy)

hist_fitx2 = gauss(bin_centresx2, *coeffx2)
hist_fity2 = gauss(bin_centresy2, *coeffy2)

hist_fitx2p = gauss(bin_centresx2p, *coeffx2p)
hist_fity2p = gauss(bin_centresy2p, *coeffy2p)


plt.subplot(611)
plt.plot(bin_centresx, histx, label='Test data')
plt.plot(bin_centresx, hist_fitx, label='Fitted data')
plt.title('posX')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean x = '
print coeffx[1]
print 'Fitted standard deviation x = '
print coeffx[2]

plt.subplot(612)
plt.plot(bin_centresy, histy, label='Test data')
plt.plot(bin_centresy, hist_fity, label='Fitted data')
plt.title('posY')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean y = '
print coeffy[1]
print 'Fitted standard deviation y= '
print coeffy[2]

plt.subplot(613)
plt.plot(bin_centresx2, histx2, label='Test data')
plt.plot(bin_centresx2, hist_fitx2, label='Fitted data')
plt.title('posY')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean x2 = '
print coeffx2[1]
print 'Fitted standard deviation x2 = '
print coeffx2[2]

plt.subplot(614)
plt.plot(bin_centresy2, histy2, label='Test data')
plt.plot(bin_centresy2, hist_fity2, label='Fitted data')
plt.title('posY')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean y2 = '
print coeffy2[1]
print 'Fitted standard deviation y2 = '
print coeffy2[2]

plt.subplot(615)
plt.plot(bin_centresx2p, histx2p, label='Test data')
plt.plot(bin_centresx2p, hist_fitx2p, label='Fitted data')
plt.title('posY')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean x2 proton = '
print coeffx2p[1]
print 'Fitted standard deviation x2 proton = '
print coeffx2p[2]

plt.subplot(616)
plt.plot(bin_centresy2p, histy2p, label='Test data')
plt.plot(bin_centresy2p, hist_fity2p, label='Fitted data')
plt.title('posY')
# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean y2 proton = '
print coeffy2p[1]
print 'Fitted standard deviation y2 proton = '
print coeffy2p[2]


plt.show()
