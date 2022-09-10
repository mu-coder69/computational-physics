import numpy as np
import matplotlib.pyplot as plt
from rootFinder import newton #function imported from rootFinder archive
plt.rcParams["font.family"] = "times new roman"


def V(r: float, derivative=False) -> float:
    r_0 = 0.741 #Armstrong
    s = 2**(-1/6) * r_0
    e = 4.75 #eV (- V_min)
    left = (s / r)**12
    right = (s / r)**6
    return 4 * e * ( left - right ) if not derivative else - 48 * e / r * ( left - right / 2)


r = np.linspace(0.5, 1.8, 200)[1:]
root = newton(lambda r: V(r, derivative=True), 0.5, error=1E-10)[0]
print(f"Equilibrium radius : {root}")


plt.hlines(0, r[0], r[-1], color="gray", linestyle="dashed")
plt.plot(r, V(r), c="k")
# plt.plot(r, V(r, derivative=True), label="Negative Force")
plt.scatter(0.741, V(0.741), marker="o", c="k")
plt.annotate(f"r = {root} $\AA$", (0.741 + 0.05, V(0.741) - 0.3))
# plt.legend()
plt.ylim(-6, 6)
plt.xlim(0.6, 1.8)
plt.xlabel("r")
plt.ylabel("U(r)")
plt.title("Lennard-Jones potential")
plt.savefig("potential.jpg", dpi=300)
# plt.show()