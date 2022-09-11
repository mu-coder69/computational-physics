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

plt.vlines(4E-8, 2E-18, 2, color="gray", linestyle="dashed")
plt.text(8E-8, 3E-17, "Critical discretization") 
plt.hlines(3E-8, 3E-13, 3, color="gray", linestyle="dashed")
plt.text(1E-3, 5E-8, "Minimum difference")
plt.loglog( h, abs(exact(b) - fwd_diff(b, y, h)), 
            c="dimgrey", 
            label="$\pi/3$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog( h, abs(exact(a) - fwd_diff(a, y, h)), 
            c="k", 
            label="$\pi/2$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.title("Forward Difference. f(x) = sin(x)")
plt.xlabel("Discretization $\it{h}$")
plt.ylabel("|Difference|")
plt.ylim(9E-18, 2)
plt.xlim(3E-13, 3)
# for i in range(len(h)):
#     print(h[i], list(abs(exact(a) - fwd_diff(a, y, h)))[i], list(abs(exact(b) - fwd_diff(b, y, h)))[i])
plt.savefig("fwd_diff.png", dpi=300)
plt.show()
# exit()
plt.vlines(3E-5, 2E-18, 1, color="gray", linestyle="dashed")
plt.hlines(3E-11, 3E-13, 3, color="gray", linestyle="dashed")
plt.text(1E-3, 5E-11, "Minimum difference")
plt.text(9E-9, 1E-1, "Critical discretization")
plt.ylim(1.4E-18, 1)
plt.xlim(3E-13, 3)
plt.loglog( h, abs(exact(b) - ctr_diff(b, y, h)), 
            c="dimgrey", 
            label="$\pi/3$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog( h, abs(exact(a) - ctr_diff(a, y, h)), 
            c="k", 
            label="$\pi/2$",
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.title("Central Difference. f(x) = sin(x)")
plt.xlabel("Discretization $\it{h}$")
plt.ylabel("|Difference|")
# for i in range(len(h)):
#     print(h[i], list(abs(exact(a) - ctr_diff(a, y, h)))[i], list(abs(exact(b) - ctr_diff(b, y, h)))[i])
plt.savefig("ctr_diff.png", dpi=300)
# print(plt.ylim())
plt.show()