import numpy as np
#------------Variables globales-----------
x_values=np.linspace(-1,1,100)[1:-1]
#-------Definición numérica--------
def f(x):
    y=1/(1-x)
    return y


def taylor(n,x):
    r=0
    for i in range(0,n):
        r=r+x**(i)
    return r
#print("x:",x,"Valor real:", "{:.8f}".format(f(x)), "Aproximación:","{:.8f}".format(taylor(200,x)))

#--------------Errores------------------
def error(x,e,fn):
    n=1
    term=fn(n, x)
    term_prev=fn(n-1,x)
    sum=term
    while abs( (term - term_prev) / sum)>e:
        n=n+1
        term=fn(n,x)
        term_prev=fn(n-1,x)
        sum=term+sum
    return n

for x in x_values:
    print(x, " ", error(x, 1E-8, taylor))