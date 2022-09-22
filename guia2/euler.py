# import matplotlib.pyplot as plt
# import numpy as np
from modules.writer import *

def func(t, y):
    alpha = -1
    return alpha*y

def euler(t, y, f, step=1E-3):
    return y + step * f(t, y)

y_0 = 1
t_0 = 0

# y = [y_0]
# t = [t_0]
h = [j*10**(-i) for i in range(1, 4) for j in range(1, 9)]
for i in range(40):
    h.append(1 + i/10)
h.sort(reverse=True)
error = []

# for h_val in h:
#     print(h_val)
#     y = [y_0]
#     t = [t_0]
#     while t[-1] < 10:
#         y.append(euler(t[-1], y[-1], func, h_val))
#         t.append(t[-1] + h_val)
#     # plt.plot(t, y, label=f"euler h={h_val}")
#     y = np.array(y)
#     t = np.array(t)
#     error.append(sum(abs(np.exp(-t) - y)))

write(h, error, path=__file__)
h = h.reshape(-1, 1)
error = error.reshape(-1, 1)
# print(f"error: {error}")

# plt.loglog(h, error, linestyle="--", marker="o")
# lim = plt.ylim()
# plt.vlines(2, lim[0], lim[1], color="gray", linestyles="dashed", linewidth=0.7)
# plt.legend()
# plt.show()