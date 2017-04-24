import numpy as np
import matplotlib.pyplot as plt

with open('Hi_in_Rb_SRIM_table.txt') as f:
    x = f.readlines()

energy=[]
de_dx_elec=[]
de_dx_nuc=[]

for i in x[23:-14]:

    ii = i.split()
    if 'GeV' in ii[1]:
        energy.append(np.double(ii[0])*1e9)
    if 'MeV' in ii[1]:
        energy.append(np.double(ii[0]) * 1e6)
    if 'keV' in ii[1]:
        energy.append(np.double(ii[0]) * 1e3)

    de_dx_elec.append(np.double(ii[2]))
    de_dx_nuc.append(np.double(ii[3]))

de_dx_elec = np.array(de_dx_elec)
de_dx_nuc = np.array(de_dx_nuc)
energy=np.array(energy)

plt.plot(np.log(energy),de_dx_elec)
ax = plt.gca()
ax.grid(True)
#plt.ylim([0,0.01])
plt.show()
