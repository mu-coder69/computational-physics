# This import registers the 3D projection, but is otherwise unused.
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



# Make data.
Nx=101
Nt=6000
# dx=0.000000001
# dt=0.000000000000000001
tf=20
dx= 3.0E-6
dt=4.6E-8

k=237
c=900
rho=2700
T=np.zeros((Nx,2),float)
TPL=np.zeros( (Nx,tf+1) ,float)

"Establecemos las condiciones de contorno"

for ix in range(1, Nx-1):    
    T[ix,0]=100 
    T[0,0]=0.0 
    T[0,1]=0 
    T[Nx-1,0]=0 
    T[Nx-1,1]=0.0

eta=(k*dt)/(c*rho*dx**2)
m=1

for t in range ( 1 , Nt ):
    for ix in range(1,Nx-1):
        T[ix,1] = T[ix,0] + eta* (T[ix+1,0] + T[ix-1,0]-2.0*T[ix,0])  
    if t%300 == 0 or t == 1 : # Cada 300 pasos
        for ix in range(1,Nx-1,2):
            TPL[ix,m]=T[ix,1]
                    
        m=m+ 1
    for ix in range(1,Nx-1):
        T[ix , 0] = T[ix , 1]
x=list(range(1,Nx-1,2)) # Plot alternate pts
y = list(range(1 , tf))
X, Y = np.meshgrid (x , y )

def functz (Tpl ) :
    z = Tpl [X, Y]
    return z
Z = functz (TPL )
# Plot the surface.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax.set_title("Solución de la ecuación de calor")
ax.set_xlabel ( 'Posición ' )
ax.set_ylabel ( 'tiempo ' )
ax.set_zlabel ( 'Temperatura ' )

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.4, aspect=5)

plt.show()


