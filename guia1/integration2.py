import numpy as np
import matplotlib.pyplot as plt

def trap_int(INTERVAL, f, N):
    integral = 0
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    if type(f(x_values)) == int:
        y_values = np.full(len(x_values), f(1))
    else: y_values = f(x_values)
    weights = np.ones(N, dtype=np.float64)/2
    for i in range(1, N):
        integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i]
    return integral*h

def simp_int(INTERVAL, f, N):
    integral = 0
    N = N +1 if N % 2 == 0 else N
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    if type(f(x_values)) == int:
        y_values = np.full(len(x_values), f(1))
    else: y_values = f(x_values)
    weights = np.ones(N, dtype=np.float64)
    weights[0::2] = 1/3
    weights[1::2] = 4/3
    for i in range(1, N, 2):
        integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i] + y_values[i+1]*weights[i+1]
    return integral*h

N = tuple([int(j*10**i) for i in range(1, 7) for j in range(1, 10)])
error_trap1 = []
error_simp1 = []
error_trap2 = []
error_simp2 = []

def func1(x):
    return x*x*x*x*x
def func2(x):
    return 1

for n in N:
    # trap = trap_int([0, 1], func1, n)
    # simp = simp_int([0, 1], func1, n)
    trap2 = trap_int([0, 1], func2, n)
    simp2 = simp_int([0, 1], func2, n)
    print(n)
    # error_trap1.append(abs( (trap - 1/6)/(1/6) ))
    # error_simp1.append(abs( (simp - 1/6)/(1/6) ))
    error_trap2.append(abs( (trap2 - 1)/1 ))
    error_simp2.append(abs( (simp2 - 1)/1 ))


# error_trap1 = np.array(error_trap1) / max(error_trap1)
# error_simp1 = np.array(error_simp1) / max(error_simp1)
error_trap2 = np.array(error_trap2) / max(error_trap2)
error_simp2 = np.array(error_simp2) / max(error_simp2)


# print(np.log(error_trap1[1:])/(np.log(N[1:]) - np.log(N[0])))
# print(np.log(error_simp1[1:])/(np.log(N[1:]) - np.log(N[0])))
print(np.log(error_trap2[1:])/(np.log(N[1:]) - np.log(N[0])))
print(np.log(error_simp2[1:])/(np.log(N[1:]) - np.log(N[0])))

plt.grid()

# plt.loglog(N, error_trap1,
#             label="Trapeze method", 
#             marker="o", 
#             markersize=3,
#             linestyle="dashed",
#             linewidth=0.7,
#             c="k")
# plt.loglog(N, error_simp1,
#             label="Simpson method", 
#             marker="o", 
#             markersize=3,
#             linestyle="dashed",
#             linewidth=0.7,
#             c="gray")
plt.loglog(N, error_trap2,
            label="Trapeze method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7,
            c="k")
plt.loglog(N, error_simp2,
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



