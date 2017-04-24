# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:08:42 2016

@author: gabrielfior
"""
import numpy as np

import scipy.integrate as integrate
from math import factorial
import matplotlib.pyplot as plt



def A_j(j,N,x):
    
    nom = np.power(x,j-1) * np.power(N,j)*np.exp(np.dot(-N,x))
    den = factorial(j-1)
    return 1.0*nom/(1.0*den)
    
x = np.linspace(0.,0.5,100)
j=range(1,6)
j=4
N=20
A2 = lambda x: np.power(x,j-1) * np.power(N,j)*np.exp(np.dot(-N,x))/(factorial(j-1))

#A = A_j(j,N,x)

int1=[]

for i in range(len(x)-1):
    integ1 = integrate.quad(A2,x[i],x[i+1])
    int1.append(integ1[0]*100)

#int1 = np.dot(100.,int1)
plt.figure(1)
plt.clf()
plt.plot(x[:-1],int1)
plt.ylabel('P (a<x<b) %')
plt.title('j = '+str(j))
plt.xlabel('x (cm)')
plt.tight_layout()
plt.show()