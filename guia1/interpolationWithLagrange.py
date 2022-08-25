import numpy as np
import matplotlib.pyplot as plt

DATA_Y = np.array([1, -1, 3, 5, 3])
DATA_X = np.array([1, 2, 3, 4, 5])

def lagrange_coefficients(i, X_VALUES):
    i_term = X_VALUES[i]
    X_VALUES = np.delete(X_VALUES, i)
    l_coef = lambda x: np.nanprod((x - X_VALUES) / (i_term - X_VALUES))
    return l_coef

L = [lagrange_coefficients(i, DATA_X) for i in range(len(DATA_X))]

def approx(x, L):
    return sum(DATA_Y[i] * L[i](x) for i in range(len(DATA_X)))

X = np.linspace(0, 8, 100)
plt.scatter(DATA_X, DATA_Y)
plt.plot(X, [approx(x, L) for x in X], linestyle="dashed")
plt.show()


