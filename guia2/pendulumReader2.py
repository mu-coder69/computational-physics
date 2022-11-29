import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})


path = r'/home/lucho/Documents/GitHub/computational-physics/guia2/data/1'

archives = [
    'pendulumODE(0.9)2.csv',
    'pendulumODE(1.075)2.csv',
    'pendulumODE(1.12)2.csv',
    'pendulumODE(1.2)2.csv',
    'pendulumODE(1.4)2.csv',
    'pendulumODE(1.45)2.csv',
    'pendulumODE(1.47)2.csv',
    'pendulumODE(1.5)2.csv',
    'pendulumODE(1.51)2.csv',
]

dataset = []

i = 1
#t = (3000, 4000)
#def p_to_time(p, h=1E-2):
#    return int(t/h)
for archive in archives:
    print(f'file {i}/{len(archives)}')
    data = np.genfromtxt(open(os.path.join(path, archive), 'rb'), 
                    delimiter=" ", 
                    names=True,
                    #skip_header=0,
                    max_rows=int(250000*0.25),
                    dtype=np.float64)

    headers = data.dtype.names
    data = np.array([data[headers[0]], data[headers[1]]]).T
    dataset.append(data)

    i += 1

fig = plt.figure()
gs = fig.add_gridspec(3, 3, hspace=0.03, wspace=0.03)

j = 0
f = [0.9, 1.075, 1.12, 1.2, 1.4, 1.45, 1.47, 1.5, 1.51]
from matplotlib.offsetbox import AnchoredText
for ax in gs.subplots(sharex='col', sharey='row'):
    for axx in ax:
        axx.scatter(dataset[j][:, 0], dataset[j][:, 1], 
            c='black', 
            marker='.',
            s=0.1)
        axx.set_ylim(-3, 3)
        axx.set_xlim(-np.pi, np.pi)
        if j not in [0, 3, 6]:
            axx.axes.get_yaxis().set_visible(False) 
        if j not in [6, 7, 8]:
            axx.axes.get_xaxis().set_visible(False) 
        if j == 7:
            axx.set_xlabel(r'$\theta$')
        if j == 3:
            axx.set_ylabel(r'$\dot{\theta}$')
        at = AnchoredText(
            rf'f = {f[j]}', prop=dict(size=10), frameon=True, loc='upper right')
        at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        axx.add_artist(at)        
        j += 1

plt.savefig('pendulo.png', dpi=400)
#plt.show()

