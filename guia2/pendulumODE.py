import numpy as np
import matplotlib.pyplot as plt
from modules.ODEsolver import RK4


def pendulum(t_interval: list, init_cond: list, params: list, h=1E-3) -> list:
    t_0, max_time = t_interval
    pos_0, vel_0 = init_cond
    B, W, F = params
    t = np.array([t_0])
    pos = np.array([pos_0])
    vel = np.array([vel_0])
    energy = np.array([get_energy(vel_0, pos_0)])
    # acc = np.array([acc_0])
    sys_vector = np.array([pos[-1], vel[-1]])
    while t[-1] < max_time:
        sys_vector = RK4(t[-1], 
                         sys_vector, 
                         lambda t, y: pendulum_eqs(t, y, B, W, F))

        pos_n, vel_n = sys_vector
        t = np.append(t, t[-1] +h)
        pos = np.append(pos, pos_n)
        vel = np.append(vel, vel_n)
        energy = np.append(energy, get_energy(vel_n, pos_n))
    return np.array([t, pos, vel, energy])

def get_energy(vel, pos):
    return vel**2/2 - np.cos(pos)

def pendulum_eqs(t, y, B=0, W=1, F=0):
    o, p = y
    dodt = p
    dpdt = -B*p - np.sin(o) + F*np.cos(W*t)
    return np.array([dodt, dpdt])

pos_0 = 0.1
vel_0 = 0 
B = 0
W = 0
F = 0
t_interval = (0, 100)
init_cond = (pos_0, vel_0)
params = (B, W, F)

system = pendulum(t_interval, init_cond, params)
plt.subplot(211)
plt.plot(system[0], system[1])
plt.plot(system[0], pos_0*np.cos(system[0]))
plt.hlines(0, plt.xlim()[0], plt.xlim()[1], color='k', linestyles="dashed")
plt.subplot(212)
plt.plot(system[0], abs( system[1] - pos_0*np.cos(system[0]) ) )
print(f"Total error: {sum(abs( system[1] - pos_0*np.cos(system[0]) ))}")
# plt.savefig("posTime.png", dpi=300)
plt.show()