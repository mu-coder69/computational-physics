
def rk4(f, y, t, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + k1/2)
    k3 = f(t + h/2, y + k2/2)
    k4 = f(t + h, y + k3)
    return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)