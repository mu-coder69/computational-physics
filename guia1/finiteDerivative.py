import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt


def exact_function(x):
    return np.exp(x)*np.log(x) - x**2


def newton(f, x_0, error=1E-8):
    f_values = []
    while abs(f(x_0)) > error:
        f_values.append(abs(f(x_0)))
        x_0 -= f(x_0) / derivative(f, x_0)
    return x_0, f_values
    

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

b = 20
limits = np.array([0, b])
bisection_root, bisection_error = bisection(exact_function, limits)
print(f"bisected root: {bisection_root}")
newton_root, newton_error = newton(exact_function, b)
print(f"newton root: {newton_root}")


plt.loglog(range(0, len(bisection_error)), bisection_error / max(bisection_error), 
            color="red", 
            label="Bisection method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.loglog(range(0, len(newton_error)), newton_error / max(newton_error), 
            color="blue", 
            label="newton-raphson method", 
            marker="o", 
            markersize=3,
            linestyle="dashed",
            linewidth=0.7)
plt.legend()
plt.show()

