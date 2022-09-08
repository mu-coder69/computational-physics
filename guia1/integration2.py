import numpy as np
import matplotlib.pyplot as plt

def trap_int(INTERVAL, f, N):
    integral = 0
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    y_values = f(x_values)
    weights = np.ones(N, dtype=np.float64)/2
    for i in range(1, N):
        integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i]
    return integral*h

def simp_int(INTERVAL, f, N):
    integral = 0
    N = N +1 if N % 2 == 0 else N
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    y_values = f(x_values)
    weights = np.ones(N, dtype=np.float64)
    weights[0::2] = 1/3
    weights[1::2] = 4/3
    for i in range(1, N, 2):
        integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i] + y_values[i+1]*weights[i+1]
    return integral*h

N = tuple([int(j*10**i) for i in range(1, 7) for j in range(1, 10)])
error_trap = []
error_simp = []


def func1(x):
    return x*x*x*x*x

for n in N:
    simp = simp_int([0, 1], func1, n)
    trap = trap_int([0, 1], func1, n)
    print(n)
    error_trap.append(abs( (trap - 1/6)/(1/6) ))
    error_simp.append(abs( (simp - 1/6)/(1/6) ))


error2 = np.array(error_trap) / max(error_trap)
error4 = np.array(error_simp) / max(error_simp)

print(np.log(error_trap[1:])/(np.log(N[1:]) - np.log(N[0])))
print(np.log(error_simp[1:])/(np.log(N[1:]) - np.log(N[0])))

plt.grid()

plt.loglog(N, error_trap,
            label="Trapeze method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7,
            c="k")
plt.loglog(N, error_simp,
            label="Simpson method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7,
            c="gray")
plt.xlabel("Iterations")
plt.ylabel("relative error")
plt.legend()
plt.show()



