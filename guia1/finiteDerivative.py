import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "times new roman"

def fwd_diff(x: float, f, h=1E-8):
    return ( f(x + h) - f(x) ) / h


def ctr_diff(x: float, f, h=1E-8):
    return ( f(x + h) - f(x - h) ) / (2 * h)
 

h = np.array([10**(-i) for i in np.arange(0.1, 12, 0.2)])
y = lambda x: np.sin(x)
exact = lambda x: np.cos(x)

a = np.pi/2
b = np.pi/3

plt.loglog( h, abs(exact(a) - fwd_diff(a, y, h)), 
            c="k", 
            label="$\pi/2$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog( h, abs(exact(b) - fwd_diff(b, y, h)), 
            c="gray", 
            label="$\pi/3$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.title("Forward Difference")
plt.xlabel("Discretization $\it{h}$")
plt.ylabel("Error")
plt.savefig("fwd_diff.png", dpi=300)
plt.show()

plt.loglog( h, abs(exact(a) - ctr_diff(a, y, h)), 
            c="k", 
            label="$\pi/2$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog( h, abs(exact(b) - ctr_diff(b, y, h)), 
            c="gray", 
            label="$\pi/3$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.title("Central Difference")
plt.xlabel("Discretization $\it{h}$")
plt.ylabel("Error")
plt.savefig("ctr_diff.png", dpi=300)
plt.show()