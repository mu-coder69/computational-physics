import matplotlib.pyplot as plt

def real(x):
    return 1 / (1 - x)

def taylor(x, limits):

    init = 0
    N_1, N_2 = limits
    for n in range(N_1, N_2+1):
        init += x**(n -1)
    return init      

error = 10**(-8)

print(" {0:<4s} | {1:<10s} | {2:<10s} | {3:<3s}".format("x", "taylor", "real", "N")) #table header
x_values = [i/100 for i in range(0, 100)]

for x in x_values:
    N = 1
    while abs(taylor(x, (N, N)) / taylor(x, (1, N))) > error:
        N += 1
    print("{0:<2.3f} | {1:<3.8f} | {2:<3.8f} | {3:<3d}".format(x, taylor(x, (1, N)), real(x), N))
    
