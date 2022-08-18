import math as m

def roots(a, b, c):
    '''
    Returns the roots of the equation ax^2 + bx + c = 0
    '''
    try: # just to handle the infinity error
        f_root = - b / (2*a) + m.sqrt(b**2 - 4*a*c)/(2*a)
    except ZeroDivisionError:
        f_root = m.inf

    try:
        s_root = - b / (2*a) - m.sqrt(b**2 - 4*a*c)/(2*a)
    except ZeroDivisionError:
        s_root = m.inf
        
    return f_root, s_root

def roots2(a, b, c):
    '''
    Returns the roots of the equation ax^2 + bx + c = 0, method 2
    '''
    try:# just to handle the infinity error
        f_root = (-2*c)/(b + m.sqrt(b**2 - 4*a*c))
    except ZeroDivisionError:
        f_root = m.inf

    try:
        s_root = (-2*c)/(b - m.sqrt(b**2 - 4*a*c))
    except ZeroDivisionError:
        s_root = m.inf

    return f_root, s_root


n = 1
c = 10**(-n)

print("{0:<5d} | {1:<10s} | {2:<10s}".format(n, "roots", "roots2")) #table header

f_roots, s_roots = roots(1, 1, c)       #store roots using method 1
f_roots2, s_roots2 = roots2(1, 1, c)    #store roots using method 2


# we are only interested in the first root, since it is equal to 0
while (f_roots != 0 or f_roots2 != 0):  #while the roots are != 0 do:

    print("{0:<5d} | {1:<10.5E} | {2:<10.5E}".format(n, f_roots, f_roots2))
    n += 1
    c = 10**(-n)
    f_roots, s_roots = roots(1, 1, c)
    f_roots2, s_roots2 = roots2(1, 1, c)

print("{0:<5d} | {1:<10.5E} | {2:<10.5E}".format(n, f_roots, f_roots2)) #print last row

