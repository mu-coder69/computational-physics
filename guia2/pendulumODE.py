import numpy as np
# import sympy as sp
from modules.ODEsolver import RK4
import modules.writer as w
from time import perf_counter, localtime, strftime

def pendulum(t_interval: list, init_cond: list, params: list, h=1E-3) -> list:
    t_0, max_time = t_interval
    pos_0, vel_0 = init_cond
    B, W, F = params
    t = np.arange(t_0, max_time, h)
    pos = pos_0 * np.ones(int((max_time - t_0)/h))
    vel = vel_0 * np.ones(int((max_time - t_0)/h))
    acc = W * np.ones(int((max_time - t_0)/h))
    sys_vector = np.array([pos_0, vel_0, acc[0]])
    for i in range(1, int((max_time - t_0)/h)):
        sys_vector = RK4(sys_vector, 
                        lambda y: pendulum_eqs(y, B, W, F),
                        h)

        # if sys_vector[0] < -np.pi:
        #     sys_vector[0] += 2*np.pi
        # elif sys_vector[0] > np.pi:
        #     sys_vector[0] -= 2*np.pi

        pos[i], vel[i], _ = sys_vector
    return np.array([t, pos, vel])

def get_energy(vel, pos):
    return vel**2/2 - 9.81**2*np.cos(pos)

def pendulum_eqs(y, B=0, W=1, F=0):
    theta, psi, omega = y
    dtheta_dt = psi
    dpsi_dt = -B*psi - np.sin(theta) + F*np.cos(omega)
    domega_dt = W
    return np.array([dtheta_dt, dpsi_dt, domega_dt])

if __name__ == '__main__':

    e = 1E-15
    pos_0 = [0.2, 0.2 + e]
    vel_0 = 0 
    B = 0.5
    W = 2/3
    #F = [1.075, 1.12, 1.4, 1.45, 1.47, 1.5, 1.51]
    F = 0.9
    t_interval = (0, 5_000)
    # init_cond = (pos_0, vel_0)

    import concurrent.futures
    #arguments = np.array([(t_interval, (pos_0[i], vel_0), (B, W, F[j]), 1E-3) for i  in range(len(pos_0)) for j in range(len(F))], dtype=object)
    arguments = np.array([(t_interval, (pos_0[i], vel_0), (B, W, F), 1E-3) for i  in range(len(pos_0))], dtype=object)
    for arg in arguments: print(arg)
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    s = perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(pendulum, 
                            arguments[:, 0],
                            arguments[:, 1],
                            arguments[:, 2],
                            arguments[:, 3])
    e = perf_counter()
    print(f'simulation finished || elapsed time: {round(e - s, 2)} s')

    headers = ['time', 'pos', 'vel', 'energy']
    i = 0
    for result in results:
        print(f'file {i +1}/{len(arguments)}')
        #result = np.concatenate([result.T, 
        #                        get_energy(result[2, :], result[1, :]).reshape(-1, 1)], 
        #                        axis=1)
        w.write(result.T, 
                name='pendulumODE' + f'({arguments[i][1][0]}-{arguments[i][2][2]})', 
                header=headers, 
                split=True, 
                keep=1, 
                path=r'/home/lucho/Documents/GitHub/computational-physics/guia2/data/00')
        i += 1

