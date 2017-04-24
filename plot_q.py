# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:39:31 2016

@author: gabrielfior
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

################################
# IMPLEMENT ENERGY TRANSFFERED MINUMUM BOUNDARY (bmin)

#####################
def calculate_distance(x1,x2,y1,y2):
    distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance
#####################

#b = np.linspace(3.53*1e-14,1e-9,1000000)
#q = 12.9*1e-22/(b**2)

#plt.plot(b,np.log(q))

n = 500
n_particles=1
v_particle = 1e-6  #m/s
range1 = -1.e-3
plotting = False
saving = False


xdist =  np.linspace(-range1,range1,n)
ydist =  np.linspace(-range1,range1,n)
X, Y = np.meshgrid(xdist, ydist, sparse=False, indexing='xy')

    
#proton exactly on center

#generate proton distribution

mu, sigma = 0, 200*1e-6 
s = np.random.normal(mu, sigma, n_particles)
list_zeros=np.zeros_like(s)*-1*range1
list_particles = np.column_stack((s,list_zeros))


A1=12.9*1e-22
#A=1.
B=1

list_times=[0.]
Z = np.zeros_like(X)
#plt.imshow(Z)
#plt.show()
#plt.ioff()
count_time=0
time=0.
total_time=10
list_time=np.arange(total_time)
list_line1=[]
list_line2=[]
listz= []

#xp,yp = 
count1=0
v = 4.e-5
xp0 = 0.
yp0 = 0.
#list_particles=[(-range1/2,0),(range1/2,0)]
for time in np.arange(10):
    Z = np.zeros_like(X)
    for particle in list_particles:
#for xp,yp in [(0,0),(.2*1e-5,0),(.4*1e-5,0),(.6*1e-5,0),(.8*1e-5,0)]:

#xp = i[1]
#yp=i[0] + v_particle*time
        xp=particle[0]
        yp=particle[1] + v*time

        Z += (A1/(np.sqrt((X-xp)**2 + (Y-yp)**2)+1e-30))
    #plt.imshow(np.log(Z))
    plt.figure(1)
    plt.clf()
    plt.subplot(111)
    plt.title('Distribution of log(EnergyDepos)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.imshow(np.log(Z))
    #plt.subplot(122)
    #cp = plt.contour(X, Y, np.log(Z))
    #plt.clabel(cp, inline=True, 
    #      fontsize=1)
    #plt.contour(np.log(Z))
    #plt.gca().invert_yaxis()
    #plt.title('Contours of log(EnergyDepos)')
    #plt.savefig('plot'+str(count1)+'.png')

    plt.show()
    #plt.imsave('out'+str(count1)+'.png',np.log(Z), format='png')
    count1+=1    
#plt.imshow(Z)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.pause(1)
#plt.colorbar()
print Z.shape
#listz.append(Z)
#plt.imsave('out'+str(time)+'.png',Z, format='png')
line1 = Z[:,int(n/2)]
line2 = Z[int(n/2),:]         
list_line1.append(line1)
list_line2.append(line2)
           

print 'here'
#plt.ion()
print 'here2'
#plt.figure(1)
#im = plt.imshow((Z), interpolation='bilinear', origin='lower',
#                cmap=cm.RdYlGn)
#plt.colorbar()
if plotting:
    fig = plt.figure()
    print 'oi'
    ax = fig.gca(projection='3d')
    print 'oi2'
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    plt.xlabel('x')
    plt.ylabel('y')
    print 'oi3'
    plt.draw()

#fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.show()
if saving:
    plt.figure(2)
    count_save=0
    for i in range(len(list_line2)):
        plt.plot(list_line2[i])
        plt.imsave(Z, 'myName'+str(count_save)+'.jpg')
        count_save+=1