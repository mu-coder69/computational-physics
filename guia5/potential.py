import numpy as np
import matplotlib.pyplot as p


n, m = 100, 100

V = np.zeros((n, m), float)

V[:, -1] = 1

Niter = 2000
for iter in range(Niter):
    for  i in range(n -2, 1, -1):
        for j in range(m -2, 1, -1):
            V[i, j] = 0.25 * ( V[i+1 ,j]+V[i-1 , j ]+V[ i , j +1]+V[ i , j - 1 ])

x = range(0 , n-1 , 2) ; y = range( 0 , m-1 , 2 )
X, Y = np.meshgrid( x , y )
def functz(V):
    z = V[X , Y]
    return z

Z = functz(V)
fig = p.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X , Y , Z , antialiased=True)
ax.set_xticks(np.arange(0, n+1, 20))
ax.set_xticklabels(np.arange(0, n+1, 20)/n)
ax.set_yticks(np.arange(0, n+1, 20))
ax.set_yticklabels(np.arange(0, n+1, 20)/n)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel( 'U(x, y)' )
p.show()

exit()

V = np.zeros((n, m), float)

V[:, -1] = 1
V[:,  0] = 1
V[0, :] = 1
V[-1, :] = 1

Niter = 2000
for iter in range(Niter):
    for  i in range(1, n -2):
        for j in range(1, m -2):
            V[i, j] = 0.25 * ( V[i+1 ,j]+V[i-1 , j ]+V[ i , j +1]+V[ i , j - 1 ]) + np.pi

x = range(0 , n-1 , 2) ; y = range( 0 , m-1 , 2 )
X, Y = np.meshgrid( x , y )
def functz(V):
    z = V[X , Y]
    return z

Z = functz(V)
fig = p.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X , Y , Z , antialiased=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel( 'Potential' )
p.show()
