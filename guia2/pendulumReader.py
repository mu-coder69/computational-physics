import os
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\00'
# path2 = r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data\3'

archives = [
    # 'pendulumODE(0.2)0.csv',
    # 'pendulumODE(0.2)2.csv',
    # 'pendulumODE(0.2)3.csv',
    # 'pendulumODE(0.201)0.csv',
    # 'pendulumODE(0.201)2.csv',
    # 'pendulumODE(0.201)3.csv',
    'pendulumODE(0.2-1.2)0.csv',
    'pendulumODE(0.2-1.2)2.csv',
    # 'pendulumODE(0.2-1.2)3.csv',
    'pendulumODE(0.201-1.2)0.csv',
    'pendulumODE(0.201-1.2)2.csv',
    # 'pendulumODE(0.201-1.2)3.csv',

]

dataset = []

i = 1
t = (3000, 4000)
def time_to_index(t, h=1E-2):
    return int(t/h)
for archive in archives:
    print(f'file {i}/{len(archives)}')
    data = np.genfromtxt(open(os.path.join(path, archive), 'rb'), 
                    delimiter=" ", 
                    names=True,
                    skip_header=time_to_index(t[0]),
                    max_rows=int((t[1] - t[0])/1E-2), 
                    dtype=np.float64)

    headers = data.dtype.names
    data = np.array([data[headers[0]], data[headers[1]]]).T
    dataset.append(data)

    i += 1



fig, (ax1, ax2, ax3, ax4) = plt.subplots(4) 

ax1.plot(dataset[0][:, 1], dataset[0][:, 0])
ax1.plot(dataset[2][:, 1], dataset[2][:, 0])

# plt.show()

diff = abs(dataset[1] - dataset[3])
dx = diff[:, 0]
dv = diff[:, 1]
ax2.plot(np.arange(t[0], t[1], 1E-2), dx)
# plt.legend()
# plt.axis('equal')
# plt.show()

ax3.plot(np.arange(t[0], t[1], 1E-2), dv)

sigma = np.log(dx/dx[0])
sigma = [sigma[n -1] / n for n in range(1, len(sigma)+1)]
print(sigma)

ax4.plot(np.arange(t[0], t[1], 1E-2), sigma)
plt.show()
# print(dx[0])
# sigma = np.log(dx / 1E-2)

# plt.semilogy(np.arange(0, len(dx)), dx)
# print(sigma[-1])
# plt.show()


