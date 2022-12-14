def euler(t, y, f, h=1E-3):
    return y + h * f(t, y)

def RK4(y: list, f, h=1E-3) -> list:
    k1 = h * f(y)
    k2 = h * f(y + k1/2)
    k3 = h * f(y + k2/2)
    k4 = h * f(y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6



