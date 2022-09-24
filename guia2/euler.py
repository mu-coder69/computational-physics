import matplotlib.pyplot as plt
import numpy as np

def func(t, y):
    alpha = -1
    return alpha*y

def euler(t, y, f, step=1E-3):
    return y + step * f(t, y)

y_0 = 1
t_0 = 0

y = [y_0]
t = [t_0]
h = 0.1
while t[-1] < 10:
    y.append(euler(t[-1], y[-1], func, h))
    t.append(t[-1] + h)

y = np.array(y)
t = np.array(t)

plt.plot(t, y, label="euler method")
plt.plot(t, np.exp(-t), label="exact")
plt.legend()
plt.show()
