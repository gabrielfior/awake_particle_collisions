import os
import numpy as np
from matplotlib import pyplot as plt

with open(os.getcwd()+'/Rb_300MeV/COLLISON.txt') as f:
    x=f.readlines()

print 'Len' + str(len(x))

list1=[]
list2 = []
for ii,jj in enumerate(x):
    if 'For' in jj:
        list1.append(jj)
        list2.append(x[ii+3])
#print list2

vac=[]
for i in list2:
    vac.append(np.double(i.split()[3]))

vac = np.array(vac)

avg_vac = np.ones_like(vac)*np.double(list2[-1].split()[-2])
median_vac = np.ones_like(vac)*np.median(vac)

print 'average ' + str(avg_vac)

plt.figure(1)
plt.title('Histogram of protons with energy 300 MeV against Rb target 10 mm long')
plt.hist(vac, bins=3)
plt.xlabel('Number of vacancies created')
plt.ylabel('Number of ocurrances')
plt.show()

plt.figure(2)
plt.plot(vac,'o',label='Collisions')
plt.title('Number of vacancies created by protons with energy 300 MeV against Rb target 10 mm long')
plt.xlabel('Ion number')
plt.ylabel('Vacancies created')

plt.plot(avg_vac,'r',label='Mean')
plt.plot(median_vac,'r',label='Median')

plt.legend
plt.show()