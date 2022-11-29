import os
import numpy as np
import matplotlib.pyplot as plt

path = r'/home/lucho/Documents/GitHub/computational-physics/guia2/data/00'
# path2 = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\3'

archives = [
    # 'pendulumODE(0.2)0.csv',
    # 'pendulumODE(0.2)2.csv',
    # 'pendulumODE(0.2)3.csv',
    # 'pendulumODE(0.201)0.csv',
    # 'pendulumODE(0.201)2.csv',
    # 'pendulumODE(0.201)3.csv',
    'pendulumODE(0.2-1.51)0.csv',
    #'pendulumODE(0.2-1.075)2.csv',
    # 'pendulumODE(0.2-1.2)3.csv',
    'pendulumODE(0.20000001-1.51)0.csv',
    #'pendulumODE(0.20000001-1.075)2.csv',
    # 'pendulumODE(0.201-1.2)3.csv',

]

dataset = []

i = 1
t = (3000, 4000)
def tti(t, h=1E-3):
    return int(t/h)
for archive in archives:
    print(f'file {i}/{len(archives)}')
    data = np.genfromtxt(open(os.path.join(path, archive), 'rb'), 
                    delimiter=" ", 
                    names=True,
                    #skip_header=tti(t[0]),
                    max_rows=tti(1050), 
                    dtype=np.float64)

    headers = data.dtype.names
    data = np.array([data[headers[0]], data[headers[1]]]).T
    dataset.append(data)

    i += 1



fig, (ax4) = plt.subplots(1) 

t0 = dataset[0][0, 1]
tl = dataset[0][-1, 1]
print('t0:', t0)

# pos - time plot
#ax1.plot(dataset[0][:, 1], dataset[0][:, 0])
#ax1.plot(dataset[2][:, 1], dataset[2][:, 0])

# diff plot
dx = abs(dataset[0][:, 0] - dataset[1][:, 0])
#ax2.semilogy(dataset[0][dx != 0, 1], dx[dx != 0])
#ax3.semilogy(dataset[0][:, 1], dv)

# sigma plot
sigma1 = np.log(dx/1E-8)
sigma = -0.015
print('t-1:', max(dataset[0][sigma1 != float('-inf'), 1])) 
#exit()
for t, s, d in zip(dataset[0][sigma1 != float('-inf'), 1], sigma1[sigma1 != float('-inf')], dx[sigma1 != float('-inf')]):
    print(t, s/t, d)
ax4.scatter(dataset[0][sigma1 != float('-inf'), 1], np.divide(sigma1[sigma1 != float('-inf')], dataset[0][sigma1 != float('-inf'), 1]), s=0.1, c='k')
ax4.set_ylim((-0.15, 0.15))
ax4.set_ylabel(r'$|\delta x(t) / \delta x_0| / t$')
ax4.set_xlabel(r'$t$')

from matplotlib.offsetbox import AnchoredText
ax4.axhline(sigma, 0, max(dataset[0][sigma1 != float('-inf'), 1]), linestyle='--', c='gray')
ax4.axhline(0, 0, max(dataset[0][sigma1 != float('-inf'), 1]), c='k')
at = AnchoredText(
    rf'$\sigma_1 = {sigma}$', prop=dict(size=10), frameon=True, loc='upper right')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax4.add_artist(at)

ratio = .3
x_left, x_right = ax4.get_xlim()
y_low, y_high = ax4.get_ylim()
ax4.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
#plt.tight_layout()
plt.savefig("sigma1.51.png", dpi=300)
#plt.show()



