import re
import numpy as np
from aux_mpp import calculate_mean_dist_from_dict_dists, gauss
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#dir1 = os.getcwd()+'/H_into_Si_300MeV/'
dir1 = os.getcwd()+'/Rb_300MeV/H_Rb_Detailed_B/'
filename = 'COLLISON.txt'

a = []
with open(dir1+filename) as outfile:
    x = outfile.readlines()


listnew=[]
recoil = []

for i in x:
    if i [0] == '\xb3' and 'Summary' not in i:
        listnew.append(i)



for ii in listnew:
    recoil.append(np.float(ii.split("\xb3")[-3]))

recoil = np.array(recoil)
#recoil.min = 25
#recoil.max = 87823
#recoil.mean() = 213
