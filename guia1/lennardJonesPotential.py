import numpy as np
import matplotlib.pyplot as plt
from rootFinder import bisection #function imported from rootFinder archive

def V(r: float, derivative=False) -> float:
    r_0 = 0.741 #Armstrong
    s = 2**(-1/6) * r_0
    e = 4.75 #eV (- V_min)
    left = (s / r)**12
    right = (s / r)**6
    return 4 * e * ( left - right ) if not derivative else  - 48 * e / r * ( left - right / 2)


r = np.linspace(0, 1, 100)[1:]
root = bisection(lambda r: V(r, derivative=True), (r[0], r[-1]))[0]

plt.grid(True, linewidth=0.7, color="darkgray")
plt.plot(r, V(r), label="Potential")
# plt.plot(r, V(r, derivative=True), label="Negative Force")
plt.scatter(0.741, V(0.741))
plt.legend()
plt.ylim(-6, 6)
plt.xlim(0.5, 1)
plt.show()