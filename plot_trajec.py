import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from aux_mpp import read_txt
from itertools import groupby
import numpy as np
from cycler import cycler
import collections
import matplotlib.cm as cm



col1 = read_txt('/Users/gabrielfior/data_mpp/Rb_300MeV/H_Rb_Detailed_B/EXYZ.txt')

plot_on = True

ion_number = []
energy = []
depth = []
elec_stop_power = []
energy_lost_last = []


for i,j in enumerate(col1):

    try:

        c = int(j.split()[0])

        a = j.split()
        ion_number.append(a[0])
        energy.append(a[1]) #eV
        depth.append([a[0],np.float(a[2])*1e-8, np.float(a[3])*1e-4, np.float(a[4])*1e-4]) #X cm, Y, Z microm
        elec_stop_power.append(np.float(a[5]))
        energy_lost_last.append(a[6])

    except ValueError:
        pass
    except IndexError:
        pass


depth1 = []
for i,j in enumerate(depth):
    if int(j[0])==1:
        depth1.append(depth[i])
    else:
        break

dict1 = collections.defaultdict(list)

for i in depth:
    #print i
    dict1[int(i[0])].append(i)


#Run through 5 itens
atoms_list = np.arange(5)+1

plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y']) +
                           cycler('linestyle', ['-', '--', ':', '-.'])))


if plot_on:

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = iter(cm.rainbow(np.linspace(0, 1, len(dict1.keys()))))
    frame1 = plt.gca(projection='3d')

    #for atom,_ in dict1.iteritems():
    for atom in atoms_list:
        depth1 = np.array(dict1[atom])

        #depth1 = np.array(depth1)
        depth1 = np.vstack(depth1[:, :]).astype(np.float)


        ax.scatter(depth1[:,1] ,depth1[:,2], depth1[:,3], marker='o',color=next(colors))

        #frame1.axes.get_xaxis().set_ticks([])
        #frame1.axes.get_yaxis().set_visible(False)
        #frame1.axes.get_zaxis().set_visible(False)

    #frame1.set_zticks([])
    ax.set_xticklabels = False
    ax.set_xlabel('X (Depth) - cm')
    ax.set_ylabel('Y - um')
    ax.set_zlabel('Z - um')

    plt.show()

