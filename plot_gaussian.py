# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:05:32 2016

@author: gabrielfior
"""
import numpy as np
import matplotlib.pyplot as plt


x= np.linspace(-2.,2.,1000)
y = np.linspace(-2.,2.,1000)
xabs = np.abs(x)
r = np.sqrt(x**2 + y**2)
mu=0.0
sig=0.2
gaussx = np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
gaussy = np.exp(-np.power(y - mu, 2.) / (2 * np.power(sig, 2.)))



gauss1 = np.sqrt(gaussx**2 + gaussy**2)

plt.subplot(121)
plt.plot(x,gaussx,'r')
#plt.plot(y,gaussy,'b')
plt.subplot(122)
plt.hist(r,weights=gauss1,bins=100)
plt.show()
