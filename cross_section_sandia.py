# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:32:09 2016

@author: gabrielfior
"""

"""
00506 // 37 - Rubidium - Rb - 10
00507 
00508 { 0.01,         0.4606E+04,  0.0000E+00,  0.0000E+00,  0.0000E+00 } ,
00509 { 0.0305,       0.1441E+04, -0.1761E+03,  0.6821E+01,  0.4470E-01 } ,
00510 { 0.111,       -0.6763E+03,  0.6772E+04, -0.1372E+04,  0.7035E+02 } ,
00511 { 0.3,         -0.3457E+03,  0.2591E+04,  0.1242E+04, -0.3481E+03 } ,
00512 { 1.805,        0.3524E+03, -0.3194E+04,  0.1657E+05,  0.1224E+05 } ,
00513 { 1.863,       -0.4025E+03,  0.1067E+05,  0.8396E+04, -0.2275E+04 } ,
00514 { 2.065,        0.5234E+01,  0.7494E+03,  0.5033E+05, -0.4276E+05 } ,
00515 { 15.2,        -0.2207E+01,  0.2653E+03,  0.6269E+06, -0.3163E+07 } ,
00516 { 100.0,        0.1101E+01, -0.4280E+03,  0.6664E+06, -0.3481E+07 } ,
00517 { 500.0,        0.3467E+00,  0.4515E+03,  0.3525E+06,  0.2783E+08 } ,


#argon
#https://www-zeuthen.desy.de/geant4/geant4.9.3.b01/G4StaticSandiaData_8hh-source.html
// 18 - Argon - Ar - 7      new
00299 
00300 // C   0.01,     0.1275E+05,  0.0000E+00,  0.0000E+00,  0.0000E+00,
00301 // C   0.0302,  -0.1674E+04,  0.1047E+04, -0.9010E+02,  0.2166E+01,
00302 
00303 { 0.01,        -8.294E+04,   5.720E+03,  -1.101E+02,   6.668E-01  } ,
00304 { 0.04,        -1.401E+03,   9.577E+02,  -7.842E+01,   1.797E+00  } ,
00305 { 0.245,       -0.2244E+03,  0.1388E+04,  0.2571E+04, -0.5113E+03 } ,
00306 { 3.203,       -0.1446E+02,  0.4359E+03,  0.6578E+05, -0.7284E+05 } ,
00307 { 20.0,         0.8786E+00, -0.3001E+03,  0.7682E+05, -0.1219E+06 } ,
00308 { 100.0,        0.6779E-01, -0.2695E+02,  0.5069E+05,  0.5281E+06 } ,
00309 { 500.0,        0.2598E-01,  0.3454E+02,  0.1059E+05,  0.1068E+08 } ,
"""

import numpy as np
import matplotlib.pyplot as plt
from plot_F_E import beta_from_energy


def return_sandia_value(E,material='Rb'):
    sandia_Rb = np.array((
[0.01,0.4606E+04,0.0000E+00,0.0000E+00, 0.0000E+00],
[0.0305,       0.1441E+04, -0.1761E+03,  0.6821E+01,  0.4470E-01 ] ,
[ 0.111,       -0.6763E+03,  0.6772E+04, -0.1372E+04,  0.7035E+02 ] ,
[ 0.3,         -0.3457E+03,  0.2591E+04,  0.1242E+04, -0.3481E+03] ,
[1.805,        0.3524E+03, -0.3194E+04,  0.1657E+05,  0.1224E+05 ] ,
[ 1.863,       -0.4025E+03,  0.1067E+05,  0.8396E+04, -0.2275E+04 ] ,
[2.065,        0.5234E+01,  0.7494E+03,  0.5033E+05, -0.4276E+05 ] ,
[15.2,        -0.2207E+01,  0.2653E+03,  0.6269E+06, -0.3163E+07 ] ,
[100.0,        0.1101E+01, -0.4280E+03,  0.6664E+06, -0.3481E+07 ] ,
[ 500.0,        0.3467E+00,  0.4515E+03,  0.3525E+06,  0.2783E+08 ] 
    ))    
    sandia_Ar = np.array((
    [ 0.01,        -8.294E+04,   5.720E+03,  -1.101E+02,   6.668E-01  ] ,
 [ 0.04,        -1.401E+03,   9.577E+02,  -7.842E+01,   1.797E+00  ] ,
 [ 0.245,       -0.2244E+03,  0.1388E+04,  0.2571E+04, -0.5113E+03 ] ,
 [ 3.203,       -0.1446E+02,  0.4359E+03,  0.6578E+05, -0.7284E+05 ] ,
 [ 20.0,         0.8786E+00, -0.3001E+03,  0.7682E+05, -0.1219E+06 ] ,
 [ 100.0,        0.6779E-01, -0.2695E+02,  0.5069E+05,  0.5281E+06 ] ,
  [500.0,        0.2598E-01,  0.3454E+02,  0.1059E+05,  0.1068E+08 ] 
))

    if material=='Rb':
        sandia=sandia_Rb
    elif material=='Ar':
        sandia=sandia_Ar

    index1 = sandia.shape[0]
    index_return = index1-1
    try:
        for i in range(index1):
            if E == sandia[i,0]:
                index_return = i
            elif E>sandia[i,0] and E<sandia[i+1,0]:
                index_return = i
            elif E>sandia[-1,0]:
                index_return=index1-1
                break
            elif E<sandia[0,0]:
                index_return=0
                break
            
    except IndexError:
        pass
        
    list1 = list(sandia[index_return])
    list1=list1[1:]
    #print list1
    sum_terms = 0.
    #print E
    for i,j in enumerate(list1):
        
        sum_terms += j/np.power(E,(i+1))  
    
    
    #return sandia[index_return], sum_terms
    return E,sum_terms
    
print 'calc'
print return_sandia_value(0.01,'Ar')
    
plotting = True
#w = np.linspace(1.e-2,10.,10000) #to be given in keV
#deltaw = w[2]-w[1]
#list_cross_sec=[]
#for energy in w:
#    array1 = return_sandia_value(energy,material='Ar')
#    list1 = list(array1)
#    sum_terms = 0.
#    for i,j in enumerate(list1):
#        
#        sum_terms += j*pow(energy,-(i+1))         
#                        
#
#    list_cross_sec.append([energy,sum_terms])
#
#
#array_energy_cross = np.array(list_cross_sec)

list1=[]
for energy in np.linspace(0.01,10.,10000):
    
    list1.append([energy,return_sandia_value(energy,material='Ar')[1]])

array_energy_cross = np.array(list1)
array_energy_cross[:,1] /= (0.15*1e23)

#OK Calculate expression - sum a_k*w-1 
#Plotting
if plotting:
    plt.figure(1)
    
    plt.clf()
    plt.title('Photoabsorption cross section (PAI) for Argon')
    plt.xlabel('Energy (eV)')
    plt.ylabel('Log10 PAI cross-section (10^-18 cm^2)')
    #plt.scatter(np.log10(array_energy_cross[:,0]*1e3),np.log10(array_energy_cross[:,1]),c='blue')
    #plt.scatter(np.log10(array_energy_cross[:,0]*1e3),np.log10(array_energy_cross[:,1]))
    plt.loglog(array_energy_cross[:,0]*1e3, 1.e18*(array_energy_cross[:,1]))
    plt.tight_layout()
    #plt.xlim([-0.0001,array_energy_cross[:,0].max()])

# Calculate full expression for dsigma/dsigmai
# Get simple figures (eg Argon)


    
    