import os
import numpy as np
from matplotlib.pyplot import *

#dir1 = os.getcwd() + "/IONIZ.txt"
#filename ='/Users/gabrielfior/data_mpp2/Rb_300MeV/H_Rb_300MeV_C/Monolayer_H_Rb_300MeV/H_Rb_300MeV_Monolayer/EXYZ.txt' 
filename ='/Users/gabrielfior/data_mpp2/Rb_300MeV/H_Rb_300MeV_C/Monolayer_H_Rb_300MeV/H_Rb_300MeV_Monolayer/IONIZ.txt' 
filename = '/Users/gabrielfior/data_mpp2/Rb_10GeV_normal_density_Monolayer/IONIZ.txt' 
filename = '/Users/gabrielfior/data_mpp2/Rb_300MeV/IONIZ.txt' 


#10 GeV
#datampp2/Rb_10GeV_normal_density_monolayer_ECYZ.txt

print 'Reading ... ' + filename
with open(filename) as f:
    x=f.readlines()

x = x[28:]



target=[]
ions=[]
recoils=[]
#del(lines1[0])
for i in x:
    
    
    target.append(np.double(i.split(' ')[0]))
    ions.append(np.double(i.split(' ')[2]))
    recoils.append(np.double(i.split(' ')[4][:i.split(' ')[4].index('\r')]))

target=np.array(target)
ions=np.array(ions)
recoils = np.array(recoils)


dists = np.ones_like(ions)*target[0]
sum_ioniz = (ions*dists).sum() / 1e6 #eV
print 'Ionization: '+str(sum_ioniz)[:4] + ' MeV'

"""
ions_arr = np.array(ions)
recoils_arr = np.array(recoils)


f = figure(1)
plot(target,ions,label='ions')
plot(target,recoils,label='recoils')
xlabel('Target in Angstrons')
ylabel('eV / (Angstron-Ion)')
title('He into Gas Ionization')
legend()
show()
"""