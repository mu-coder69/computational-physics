import numpy as np
from modules.ODEsolver import RK4
import modules.writer as w


def pendulum(t_interval: list, init_cond: list, params: list, h=1E-3) -> list:
    t_0, max_time = t_interval
    pos_0, vel_0 = init_cond
    B, W, F = params
    t = np.array([t_0])
    pos = np.array([pos_0])
    vel = np.array([vel_0])
    acc = np.array([W])
    energy = np.array([get_energy(vel_0, pos_0)])
    # acc = np.array([acc_0])
    sys_vector = np.array([pos[-1], vel[-1], acc[-1]])
    while t[-1] < max_time:
        sys_vector = RK4(sys_vector, 
                         lambda y: pendulum_eqs(y, B, W, F))

        if sys_vector[0] < -np.pi:
            sys_vector[0] += 2*np.pi
        elif sys_vector[0] > np.pi:
            sys_vector[0] -= 2*np.pi
        pos_n, vel_n, acc_n = sys_vector
        t = np.append(t, t[-1] +h)
        pos = np.append(pos, pos_n)
        vel = np.append(vel, vel_n)
        acc = np.append(acc, acc_n)
        energy = np.append(energy, get_energy(vel_n, pos_n))
    return np.array([t, pos, vel, energy])

def get_energy(vel, pos):
    return vel**2/2 - 9.81**2*np.cos(pos)

def pendulum_eqs(y, B=0, W=1, F=0):
    theta, psi, omega = y
    dtheta_dt = psi
    dpsi_dt = -B*psi - np.sin(theta) + F*np.cos(omega)
    domega_dt = W
    return np.array([dtheta_dt, dpsi_dt, domega_dt])

pos_0 = 0.2
vel_0 = 0 
B = 0.5
W = 2/3
F = [0.9, 1.075, 1.12, 1.2, 1.4, 1.45, 1.47, 1.5, 1.51]
t_interval = (0, 600)
init_cond = (pos_0, vel_0)
# params = (B, W, F)
step = 16
dump = int(400/1E-2/step)

for i in range(len(F)):
    params = (B, W, F[i])
    system = pendulum(t_interval, init_cond, params, h=1E-2)
    system = w.optimize(system.T, step)
    system = w.dump(system, dump)
    headers = ['time', 'pos', 'vel', 'energy']
    w.write(system, 
            name='pendulumODE' + f'({F[i]})', 
            header=headers, 
            split=True, 
            keep=1, 
            path=r'C:\Users\luciano\Documents\GitHub\computational-physics\guia2\data')