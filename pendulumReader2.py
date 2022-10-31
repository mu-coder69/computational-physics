import os
import numpy as np
import matplotlib.pyplot as plt

path = r'/media/lucho/4698D38C98D3793F/Users/luciano/Documents/GitHub/computational-physics/guia2/data/1'
# path2 = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\3'

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
gs = fig.add_gridspec(3, 3, hspace=0, wspace=0)

j = 0
for ax in gs.subplots(sharex='col', sharey='row'):
	for axx in ax:
		axx.scatter(dataset[j][:, 0], dataset[j][:, 1], 
			c='black', 
			marker='.',
			s=0.1)
		if j not in [0, 3, 6]:
			axx.axes.get_yaxis().set_visible(False)	
		if j not in [6, 7, 8]:
			axx.axes.get_xaxis().set_visible(False)	
					
		j += 1

#ax1.scatter(dataset[0][:, 0],dataset[0][:, 1], c='black', s=0.2)
#ax8.scatter(dataset[1][:, 0],dataset[1][:, 1], c='black', s=0.2)
plt.tight_layout()
plt.savefig('pendulo.png', dpi=400)
#plt.show()

#fig, (ax1, ax2, ax3, ax4) = plt.subplots(4) 

#ax1.plot(dataset[0][:, 1], dataset[0][:, 0])
#ax1.plot(dataset[2][:, 1], dataset[2][:, 0])

# plt.show()

#diff = abs(dataset[1] - dataset[3])
#dx = diff[:, 0]
#dv = diff[:, 1]
#ax2.plot(np.arange(t[0], t[1], 1E-2), dx)
# plt.legend()
# plt.axis('equal')
# plt.show()

#ax3.plot(np.arange(t[0], t[1], 1E-2), dv)

#sigma = np.log(dx/dx[0])
#sigma = [sigma[n -1] / n for n in range(1, len(sigma)+1)]
#print(sigma)

#ax4.plot(np.arange(t[0], t[1], 1E-2), sigma)
#plt.show()
# print(dx[0])
# sigma = np.log(dx / 1E-2)

# plt.semilogy(np.arange(0, len(dx)), dx)
# print(sigma[-1])
# plt.show()


