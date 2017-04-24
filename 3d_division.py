# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:46:19 2016

@author: gabrielfior
"""

import pandas as pd
import numpy as np
import graphlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


loading=False #Set True to load full csv file

full_csv_path = '/Users/gabrielfior/data_mpp2/400GeV_15steps_full.csv'

##################################
if loading:

    sf = graphlab.SFrame.read_csv(full_csv_path)    
    print sf.column_names()
    sf = sf.select_columns(['position_x','position_y','position_z','energy_deposit','dE',
                              'count_particle','particle_name'])

##################################
def get_radial_value(row):
    return np.sqrt((np.double(row['position_x'])*np.double(row['position_x']))+ (np.double(row['position_y'])*np.double(row['position_y'])))
####################################
def return_num_electrons(row,calc_string,elec_pair_in_ev):
    if calc_string=='avg':
        return np.double(row['energy_deposit'])/(elec_pair_in_ev*2.25*1.0e-6)
    if calc_string=='min':
        return np.double(row['energy_deposit'])/(elec_pair_in_ev*1.5*1.0e-6)
    if calc_string=='max':
        return np.double(row['energy_deposit'])/(elec_pair_in_ev*3.*1.0e-6)           
    else:
        return np.NaN
####################################
    
#sf2 = sf.copy()
#Dump columns not needed

print 'initial num rows: '+str(sf.num_rows())
#Filter out energy_deposits smaller than 1ev
sf_energy_deposit = sf[sf['energy_deposit']>=10.0e-6]
print 'final num rows: ' + str(sf_energy_deposit.num_rows())
#del(sf)
elec=sf[sf['particle_name']=='e-']
#Just 1 file
#sf1 = graphlab.SFrame.read_csv(fileinput1)
#sf1 = sf1.select_columns(['position_x','position_y','position_z','energy_deposit','dE',
                          #'count_particle','particle_name'])

#CHOOSE WIHICH ELEMENT TO PLOT

sf_energy_deposit['position_r'] = sf_energy_deposit.apply(get_radial_value)
sf_energy_deposit['num_e_gen'] = sf_energy_deposit.apply(lambda x: return_num_electrons(x,'avg',4.1))

x1 = np.array(sf_energy_deposit['position_x'])
y1 = np.array(sf_energy_deposit['position_y'])
z1 = np.array(sf_energy_deposit['position_z'])
r1 = np.array(sf_energy_deposit['position_r'])
en_ev = np.array(sf_energy_deposit['energy_deposit']*1e6) #eV
elec_generated = np.array(sf_energy_deposit['num_e_gen'])


#Cen3D = plt.figure(1)
#Cen3D.clf()
#ax = Cen3D.add_subplot(111, projection='3d')
#ax.scatter(x1,y1,z1,cmap='hot',s=en_ev,alpha=0.5)


#for xy in zip(x1,y1):                                       # <--
#    ax.annotate('(%s, %s)' % xy,xy=xy, textcoords='data') # <--

#2D
#fig1 = plt.figure(1)
#plt.clf()
#plt.scatter(z1,en_ev)

plt.scatter(r1, z1, s=en_ev, alpha=0.5)

ax.set_title('3D Distribution of energy deposition - dimensions in mm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
print 'the end'



'''
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

ax = subplot(111)
subplots_adjust(left=0.25, bottom=0.25)
t = arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 2.5
x = np.array(sf[sf['Z']==f0]['X'])
y = np.array(sf[sf['Z']==f0]['Y(mm)'])

#s = a0*sin(2*pi*f0*t)
l, = plot(x,y, 'o')

axis([0, 1, -10, 10])



axcolor = 'lightgoldenrodyellow'
axfreq = axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp  = axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(np.array(sf[sf['Z']==freq]['Y(mm)']))
    l.set_xdata(np.array(sf[sf['Z']==freq]['X']))    
    draw()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

#rax = axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
#radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
#def colorfunc(label):
#    l.set_color(label)
#    draw()
#radio.on_clicked(colorfunc)

show()

'''