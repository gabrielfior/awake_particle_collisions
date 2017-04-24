import matplotlib.pyplot as plt
import numpy as np
list1 = []


with open('h_in_si.txt') as f:
    x = f.readlines()


for i in x:
    if 'eV' in i and 'Stop' not in i:
        list1.append(i)
    elif 'Multiply' in i:
        break

energy = []
ele_loss = []
nuc_loss = []

for ii in list1:

    a = ii.split()
    if a[1] == 'MeV':
        energy.append(np.double(1.*np.double(a[0])))
    elif a[1] == 'eV':
        energy.append(np.double(0.000001* np.double(a[0])))
    elif a[1] == 'keV':
        energy.append(np.double(0.001 * np.double(a[0])))
    elif a[1] == 'GeV':
        energy.append(np.double(1000 * np.double(a[0])))
    else:
        energy.append(np.double(np.double(a[0])))

    ele_loss.append(a[2])
    nuc_loss.append(a[3])

energy = np.array(energy)
ele_loss = np.array(ele_loss)
nuc_loss = np.array(nuc_loss)


fig1 = plt.figure(1)
plt.plot(energy, ele_loss,'o',label='electron')
plt.plot(energy, nuc_loss,'o',label='nuclear')
plt.xlabel('MEv')
plt.ylabel('Electron Stopping power MeV/(mg/cm2)')
plt.show()

