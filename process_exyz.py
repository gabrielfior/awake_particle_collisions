# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:54:41 2016

@author: gabrielfior
"""
import json
import numpy as np
import os

#/datampp2/Rb_300MeV/EXYZ

#with open(os.getcwd()+'exyz_dict_100.txt') as json_data:
with open(os.getcwd()+'/exyz_dict_100.txt') as json_data:

    d = json.load(json_data)

energy_ion=[]
elec_stop=[]
energy_lost=[]

for id1,list1 in d.iteritems():

    for i in list1:
        if len(i)>70:
            energy_ion.append(np.double(i.split(' ')[1]))
            elec_stop.append(np.double(i.split(' ')[-3]))
            energy_lost.append(np.double(i.split(' ')[-1][:i.split(' ')[-1].index('\r')]))


energy_ion = np.array(energy_ion)
energy_lost = np.array(energy_lost)
elec_stop = np.array(elec_stop)

#define mean energy lost , mean elec_stop, final energy
count1 = 0
dict2 = {}
for i,j in d.iteritems():

    if d[i] != []:
        #final energy
        
        dict2[i] = {
            'final_energy':  np.double(d[i][-1].split(' ')[1]),
            'energy_lost': energy_lost[count1:len(d[i])].sum(),
            'elec_stop': elec_stop[count1:len(d[i])].sum()
        }        
        #print 'final energy: ' + 'ion num: ' + str(i) + ',value: '+str(np.double(d[i][-1].split(' ')[1]))
    
        #mean energy lost, mean elec_stop
        #print 'energy lost by ion # ' + str(i) +'value: ' + str(energy_lost[count1:len(d[i])].sum())
        #print 'elec stop power ion # ' + str(i) +'value: ' + str(elec_stop[count1:len(d[i])].sum())    
    count1=len(d[i])


print 'done'

#save dict


final_energy_loss = 0.0
count=0
for i,j in dict2.iteritems():
    final_energy_loss += j['final_energy'] #maybe final energy
    count+=1
    
dict2['final_energy_loss_mean'] = (final_energy_loss*1.0)/count

with open('energy_loss_exyz.txt','w') as outfile:
    json.dump(dict2,outfile,indent=4)
