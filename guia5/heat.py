import numpy as np
import matplotlib.pyplot as p

Nx = 101 ;
Nt = 6000 ;
Dx = 0.03 ;
Dt = 0.9
KAPPA = 210. ; SPH = 900. ; RHO = 2700. 
T = np.zeros((Nx,2),float); Tpl = np.zeros((Nx,31),float)
for ix in range(1,Nx-1):T[ix,0] = 100.0 ;
T[0 ,0 ] = 0.0 ;
T[0 , 1 ] = 0.
T[Nx- 1 ,0 ] = 0. ; T[ Nx- 1 ,1 ] = 0.0
cons = KAPPA / ( SPH*RHO) * Dt / ( Dx*Dx ) ;
m = 1
# Initial T
# 1st & last T = 0
# c o ns t a nt
# counter
for t in range(1,Nt):
    for ix in range( 1 , Nx - 1 ):
        T[ ix , 1 ] = T[ ix , 0 ] + cons * ( T[ ix +1 , 0 ] + T[ ix -1 , 0 ] - 2.* T[ ix , 0 ] )
    if t %300 == 0 or t == 1 :
        # Every 300 s t e p s
        for ix in range(1 , Nx - 1 , 2 ): Tpl[ix,m] = T[ ix , 1 ]
        print(m)
        m = m + 1
    for ix in range( 1 , Nx - 1 ): T[ ix , 0 ] = T[ ix , 1 ]
x = list(range( 1 , Nx - 1 , 2 ) )
# Plo t a l t e r n a t e p t s
y = list(range(1 , 30) )
X, Y = np.meshgrid( x , y )
def functz( Tpl ):
    z = Tpl[X, Y ]
    return z
Z = functz( Tpl )
fig = p.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y , Z , color='r')
ax.set_xlabel( ' P o s i t i o n')
ax.set_ylabel( 'time' )
ax.set_zlabel('Temperature')
p.show( )
print( " finished " )
# Create f i g u r e
