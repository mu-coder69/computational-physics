import math as m
import matplotlib.pyplot as plt

def sinApprox(x, N=None, recursive=True, error=1E-8):

    sum = x
    term = x
    n = N
    if N != None and recursive: # N-term recursive approximation
        for n in range(2, N+1):
            term *= - x**2 / (2*n -1) / (2*n -2)
            sum += term


    elif N != None: # N-term factorial approximation
        for n in range(2, N+1):
            sum += (-1)**n * x**(2*n -1) / m.factorial(2*n -1)


    elif recursive: # min error recursive approximation
        n = 2
        while abs(term) > error:
            term *= - x**2 / (2*n -1) / (2*n -2)
            sum += term
            n += 1

            
    else: # min error factorial approximation
        n = 2
        while abs(term) > error:
            sum += (-1)**n * x**(2*n -1) / m.factorial(2*n -1)
            n += 1

    return sum, n

N = 100
x_values = [i/N for i in range(int(-N/2), int(N/2)+1)]

print("{0:^5s} | {1:^3s} | {2:^18s} | {3:^15s}".format("x", "N", "sum", "|sum - sin(x)| / sin(x)"))

for x in x_values:
    sum, N = sinApprox(x)
    try:
        dif = abs(sum - m.sin(x)) / m.sin(x)
    except ZeroDivisionError:
        dif = 0
    print("{0: 2.2f} | {1:^3d} | {2: 10.15f} | {3: 10.15f}".format(x, N, sum, dif))
    plt.scatter(x, dif, color="red", s=1)
plt.show()
