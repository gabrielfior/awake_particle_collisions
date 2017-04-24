# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:33:59 2016

@author: gabrielfior
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as plt
import pandas as pd

a = pd.read_csv('/Users/gabrielfior/Downloads/element_fit.csv',
                sep=';')


xx= np.array(a['molar mass'])
dataxx = np.array(a['Walpha'])

N = 1000 # number of data points
t = np.linspace(0, 4*np.pi, N)
data = 3.0*np.sin(t+0.001) + 0.5 + np.random.randn(N) # create artificial data with noise

guess_mean = np.mean(dataxx)
guess_std = 500#3*np.std(dataxx)/(2**0.5)
guess_phase = 0
exp_guess = -2.

# we'll use this to plot our first estimate. This might already be good enough for you
#data_first_guess = guess_std*np.sin(t+guess_phase) + guess_mean
data_first_guess = guess_std*np.sin(xx+guess_phase)*np.exp(exp_guess*xx) + guess_mean
# Define the function to optimize, in this case, we want to minimize the difference
# between the actual data and our "guessed" parameters
optimize_func = lambda x: x[0]*np.sin(xx+x[1])*np.exp(x[3]*xx) + x[2] - dataxx
est_std, est_phase, est_mean, est_exp = leastsq(optimize_func, [guess_std, guess_phase, guess_mean, exp_guess])[0]

print exp_guess
print est_exp
print '\n'
print guess_std
print est_std

# recreate the fitted curve using the optimized parameters
data_fitxx = est_std*np.sin(xx+est_phase)*np.exp(est_exp*xx) + est_mean

plt.plot(dataxx, 'o')
plt.plot(data_fitxx, label='after fitting')
plt.plot(data_first_guess, label='first guess')
plt.legend()
plt.show()