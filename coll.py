import re
import numpy as np
from aux_mpp import calculate_mean_dist_from_dict_dists, gauss
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#dir1 = os.getcwd()+'/H_into_Si_300MeV/'
dir1 = os.getcwd()+'/Rb_300MeV/H_Rb_Detailed_B/'
#filename = 'COLLISON.txt'
filename = '/Users/gabrielfior/data_mpp2/Rb_10GeV_normal_density_Monolayer/COLLISON.txt' 

a = []
with open(filename) as outfile:
    x = outfile.readlines()


listnew=[]
energies_lost_col=[]
for j,i in enumerate(x):
    if i != "" and i[0] == '\xb3' and 'Recoils' not in i and 'Summary' not in i:
        print j
        listnew.append(i)
        energies_lost_col.append(np.double(i.split('\xb3')[-3]))
        
energies_lost_col= np.array(energies_lost_col)


"""
ion_number = []
energy=[]
depth=[]
distancey=[]
distancez=[]
seev=[]
atom_hit=[]
recoil_energy=[]

for i in listnew:

    list1 = [m.start() for m in re.finditer('\xb3', i)]
    ion_number.append(i[list1[0]+1:list1[1]])
    energy.append(i[list1[1] + 1:list1[2]])
    depth.append(i[list1[2] + 1:list1[3]])
    distancey.append(i[list1[3] + 1:list1[4]])
    distancez.append(i[list1[4] + 1:list1[5]])
    seev.append(np.float(i[list1[5] + 1:list1[6]]))
    atom_hit.append((i[list1[6] + 1:list1[7]]))
    recoil_energy.append(np.float(i[list1[7] + 1:list1[8]]))

#ion 1
dists = []
energy_calc=[]
ion_num = []

for i in range(1,len(ion_number)):
        dx = np.double(depth[i])-np.double(depth[i-1])
        dz= np.double(distancez[i]) - np.double(distancez[i-1])
        dy= np.double(distancey[i]) - np.double(distancez[i-1])
        dists.append(np.sqrt(dx*dx + dy*dy + dz*dz))
        energy_calc.append(np.double(energy[i]))
        ion_num.append(ion_number[i])

#from 0 bis 26
#ion_number = []
#energy=[]
#depth=[]
#distancey=[]
#distancez=[]
#seev=[]

dists = np.array(dists)
energy_calc=np.array(energy_calc)

#energy_loss = sum(dists*energy_calc) #in ev
#energy_loss /= 6.242*1e18
#print energy_loss
dict_energy_loss={}
dict_dists={}

for i in np.unique(ion_num):
    dict_energy_loss[str(i)] = 0.
    dict_dists[str(i)] = 0.

for i in range(len(energy_calc)):

    energy_loss = dists[i] * energy_calc[i]  # in ev
    energy_loss /= 6.242 * 1e18 #in J
    dict_energy_loss[ion_num[i]] += energy_loss
    #print ion_num[i]
    dict_dists[ion_num[i]] += dists[i]

#dict_energy_loss = contains the energy lost by all ions
list_energy_lost = []
for key,value in dict_energy_loss.iteritems():
    list_energy_lost.append([np.double(key),np.double(value)])

list_energy_lost=np.array(list_energy_lost)
list_dists = calculate_mean_dist_from_dict_dists(dict_dists)
"""
########################
# gauss fitting
#p0 = [1., 0., 1.]
#xdata = np.array(range(len(seev)))
#seev = np.array(seev)
#coeff, var_matrix = curve_fit(gauss, xdata, seev,p0=p0)
#hist_fit = gauss(xdata, *coeff)
#plt.plot(xdata, seev, label='Test data')
#plt.plot(xdata, hist_fit, label='Fitted data')
#plt.show()
#########################