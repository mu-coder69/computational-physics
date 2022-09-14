import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "times new roman"})

def trap_int(INTERVAL, f, N):
    integral = 0
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    if type(f(x_values)) == int:
        y_values = np.full(len(x_values), f(1))
    else: y_values = f(x_values)
    # weights = np.ones(N, dtype=np.float64)/2
    integral += sum(y_values[1:-1])
    integral += (y_values[0] + y_values[-1])/2 
    # for i in range(1, N):
    #     integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i]
    return integral*h

def simp_int(INTERVAL, f, N):
    integral = 0
    N = N +1 if N % 2 == 0 else N
    h = (INTERVAL[1] - INTERVAL[0])/(N -1)
    x_values = np.linspace(INTERVAL[0], INTERVAL[1], N, dtype=np.float64)
    if type(f(x_values)) == int:
        y_values = np.full(len(x_values), f(1))
    else: y_values = f(x_values)
    # weights = np.ones(N, dtype=np.float64)
    integral += 2*sum(y_values[2:-2:2])
    integral += 4*sum(y_values[1:-1:2])
    integral += y_values[0] + y_values[-1]
    # weights[0::2] = 1/3
    # weights[1::2] = 4/3
    # for i in range(1, N, 2):
    #     integral += y_values[i-1]*weights[i-1] + y_values[i]*weights[i] + y_values[i+1]*weights[i+1]
    return integral*h/3

N = tuple([j*10**i for i in range(1, 7) for j in range(1, 10)])

error_trap1 = []
error_simp1 = []
error_trap2 = []
error_simp2 = []

def func1(x):
    return x*x*x*x*x
def func2(x):
    return 1/(2*x**(1/2))

for n in N:
    trap = trap_int([0, 1], func1, n)
    simp = simp_int([0, 1], func1, n)
    # trap2 = trap_int([0.0000001, 1], func2, n)
    # simp2 = simp_int([0.0000001, 1], func2, n)
    print(n)
    error_trap1.append(abs( (trap - 1/6)/(1/6) ))
    error_simp1.append(abs( (simp - 1/6)/(1/6) ))
    # error_trap2.append(abs( (trap2 - 1)/1 ))
    # error_simp2.append(abs( (simp2 - 1)/1 ))


plt.grid()
plt.title("Integration methods. f(x) = $x^5$")
plt.vlines(1.05E6, 6E-17, 1, color="gray", linestyle="dashed", linewidth=0.8)
plt.text(6.1E5, 1E-8, "Optimum N\nTrapeze", rotation="vertical")
plt.hlines(1.6E-12, 2, 39000000, color="gray", linestyle="dashed", linewidth=0.8)
plt.text(2.7, 4E-13, "Minimum error\nTrapeze")
plt.vlines(2300, 6E-17, 1, color="gray", linestyle="-.", linewidth=0.8)
plt.text(1300, 3E-5, "Optimum N\nSimpson", rotation="vertical")
plt.hlines(6.5E-14, 2, 39000000, color="gray", linestyle="-.", linewidth=0.8)
plt.text(50, 2E-14, "Minimum error\nSimpson")
plt.ylim(6E-17, 1)
plt.xlim(2, 39000000)
plt.loglog(N, error_trap1,
            label="Trapeze method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7,
            c="k")
plt.loglog(N, error_simp1,
            label="Simpson method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7,
            c="dimgrey")
# plt.loglog(N, error_trap2,
#             label="Trapeze method", 
#             marker="o", 
#             markersize=3,
#             linestyle="dashed",
#             linewidth=0.7,
#             c="k")
# plt.loglog(N, error_simp2,
#             label="Simpson method", 
#             marker="o", 
#             markersize=3,
#             linestyle="dashed",
#             linewidth=0.7,
#             c="gray")
plt.xlabel("Intervals N")
plt.ylabel("|numerical - exact| / |exact|")
plt.legend()
plt.savefig("integration.png", dpi=300)
# exit()
plt.show()



