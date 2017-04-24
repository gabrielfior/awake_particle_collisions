# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 21:54:11 2016

@author: gabrielfior
"""

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(-2*1e-11,2*1e-11,1e3)
x,y = np.meshgrid(n,n)

r_min = 0.5e-14
r_1shell = 1.7e-11
r_2shell = 0.68e-11

r = np.sqrt(x**2+y**2)
color = np.zeros_like(r)
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r[i][j] <= r_min:
            color[i][j] = 1.
        elif r[i][j] <= r_2shell:
            color[i][j] = 2.
        elif r[i][j] <= r_1shell:
            color[i][j] = 3.


plt.imshow(color)

        