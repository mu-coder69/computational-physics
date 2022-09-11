import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "times new roman"})

def exact_function(x):
    return np.exp(x)*np.log(x) - x**2


def newton(f, x_0, error=1E-8):
    a = x_0
    b = 0
    f_values = []
    while abs(a - b) > error:
        b = a
        a = b - f(b) / derivative(f, b, dx=1E-6)
        f_values.append(abs(a - b))
    return a, np.array(f_values)
    

def bisection(f, interval, error=1E-8):
    a, b = interval
    c = None
    f_a = f(a)
    f_b = f(b)
    interval_error = []
    while abs(a - b) > error:
        if f_a * f_b < 0:
            c = abs(a+b)/2
            a, b = (a, c) if f_a * f(c) < 0 else (c, b)
            f_a, f_b = f(a), f(b)
        elif f_a * f_b == 0:
            return a if f_a == 0 else b
        interval_error.append(abs(a-b))

    return abs(a+b)/2, interval_error

plt.hlines(1E-8, 1, 60, linestyles="dashed", color="gray")
b = 50
limits = np.array([0.1, b])
bisection_root, bisection_error = bisection(exact_function, limits)
plt.title("Root finder algorithms")
plt.semilogy(range(1, len(bisection_error) +1), 
            bisection_error, 
            color="k", 
            label=f"Bisection\n[0.1, {b}]", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
marker = ["^", "s", "D"]
i = 0
for x_0 in [0.1, 20, 50]:
    # x_0 = 0.1
    # print(f"bisected root: {bisection_root}")
    newton_root, newton_error = newton(exact_function, x_0)
    # newton_error /= max(newton_error)
    # print(f"newton root: {newton_root}")
    plt.semilogy(range(1, len(newton_error) +1), 
                newton_error, 
                color="dimgrey", 
                label=f"NR \n$x_0 = ${x_0}", 
                marker=marker[i], 
                markersize=3,
                linestyle="dashed",
                linewidth=0.7)
    i += 1
plt.xlabel("Iterations")
plt.ylabel("|Error|")
plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
plt.xlim(0, 60)
plt.text(11, 2E-8, "Minimum error")
plt.savefig("newton.jpg", bbox_inches="tight", dpi=300)
# plt.show()
