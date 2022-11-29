import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import time as t
from scipy.special import hermite 

V_0=1

def x1(dim):
    val = np.sqrt(1 + np.arange(dim-1))
    a = np.diag(val, 1) + np.diag(val, -1)
    return a[:dim,:dim]

def x2(dim):
    n = np.arange(dim)
    val_a = np.sqrt((1 + n)*(2 + n))
    a = np.diag(val_a, 2) + np.diag(val_a, -2)
    val_b = 2*n + 1
    b = np.diag(val_b, 0) 
    mat = a[:dim, :dim] + b
    return mat[:dim, :dim]

def x4(dim):
    mat = x2(dim) @ x2(dim)
    for i in range(dim):
        mat[i, i] = 6*i**2 + 6*i + 3
    return mat

def p(dim):
    n = np.arange(dim)
    val_a = np.sqrt((n+1)*(n+2))
    a = np.diag(val_a, 2) + np.diag(val_a, -2)
    val_b = -2*n -1
    b = np.diag(val_b, 0)
    mat = a[:dim, :dim] + b
    return mat

def error(Dp):
    Er=[[],[],[],[]]
    En=[[],[],[],[]]
    dim0=9
    dim=np.arange(dim0,100,1,dtype=int)
    j=0
    for d in Dp:
        dimn=[]
        for i in dim:
            mtz1=x2(i)
            mtz2=x4(i)
            mtzp=p(i)
            V=4*V_0*(mtz2/(d**4)-mtz1/(d**2))
            H=V-mtzp/4
            E_n,v_n=LA.eigh(H)
            En[j].append(E_n[0])
            if i > dim0 and i%2 == 1:
                E_r=100*abs((En[j][i-dim0]-En[j][i-dim0-1])/En[j][i-dim0])
                Er[j].append(E_r)
                dimn.append(i)
        j=j+1
    return(Er,dim,dimn,En)

Dp=[0.1,1,10,30]
datos=error(Dp)
En=datos[3]
dim=datos[1]
N=datos[2]
rel=datos[0]

'''
fig, ax= plt.subplots()

ax.plot(N,rel[0],color="orange",linestyle="--",linewidth="3")
ax.plot(N,rel[1],color="royalblue",linestyle="--",linewidth="3")
ax.plot(N,rel[2],color="lightseagreen",linestyle="--",linewidth="3")
ax.plot(N,rel[3],color="crimson",linestyle="--",linewidth="3")
ax.set_yscale("log")
ax.set_xscale("log")
ax.text(N[20]+5,rel[0][20]+0.95*rel[0][20],"$D=0.1$",fontsize=15,bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 3})
ax.text(N[20]+6,rel[1][20]+0.1*rel[1][20],"$D=1$",fontsize=15,bbox={'facecolor': 'royalblue', 'alpha': 0.5, 'pad': 3})
ax.text(N[20]+2,rel[2][20]+0.2*rel[2][20],"$D=10$",fontsize=15,bbox={'facecolor': 'lightseagreen', 'alpha': 0.5, 'pad': 3})
ax.text(N[20]+2,rel[3][20]-0.9*rel[3][20],"$D=30$",fontsize=15,bbox={'facecolor': 'crimson', 'alpha': 0.5, 'pad': 3})
ax.set_xlabel("Dimensión")
ax.set_ylabel("$Error relativo$")
plt.savefig("Error1",dpi=600)
plt.show()

'''

def EvsD(D):
    E=[[],[],[]]
    v=[[[],[]],[[],[]],[[],[]]]
    j=0
    for d in D:
        E_r=1
        dim0=3
        dim=dim0
        ctl=[]
        while E_r > 10**(-1):
            mtz1=x2(dim)
            mtz2=x4(dim)
            mtzp=p(dim)
            V=4*V_0*(mtz2/(d**4)-mtz1/(d**2))
            H=V-mtzp/4
            E_n,v_n=LA.eigh(H)
            ctl.append(E_n[0])
            if dim > dim0 and dim%2 == 1:
                E_r=100*abs((ctl[dim-dim0]-ctl[dim-dim0-1])/ctl[dim-dim0])
            dim=dim+1
        E[0].append(E_n[0])
        E[1].append(E_n[1])
        E[2].append(E_n[2])
        v[0][j].append(v_n[0])
        v[1][j].append(v_n[1])
        v[2][j].append(v_n[2])
        j += 1
    return(E,v) 

D=np.arange(0.5,15,0.5)
E=EvsD(D)

E0=E[0]
E1=E[1]
E2=E[2]

fig, ax= plt.subplots(3,1)
ax[0].plot(D,E0,label="$E_0$",linewidth=2.5)
ax[1].plot(D,E1,label="$E_1$",linewidth=2.5)
ax[2].plot(D,E2,label="$E_2$",linewidth=2.5)
ax.set_xlabel("$D$",fontsize=15)
ax.set_ylabel("Niveles de Energía",fontsize=13)
plt.legend(fontsize=15)
plt.savefig("figura3",dpi=400)
plt.show()


def E1vsD(D,E0):
    E=[[],[],[]]
    v=[[],[],[]]
    d=D
    E_r=2
    dim0=3
    dim=dim0
    ctl=[]
    while E_r > 10**(-1):
        mtz1=x2(dim)
        mtz2=x4(dim)
        mtzp=p(dim)
        mtzx=x1(dim)
        V=4*V_0*(mtz2/(d**4)-mtz1/(d**2))+E0*mtzx/(sqrt(2)*d)
        H=V-mtzp/4
        E_n,v_n=LA.eigh(H)
        ctl.append(E_n[0])
        if dim > dim0 and dim%2 == 1:
            E_r=100*abs((ctl[dim-dim0]-ctl[dim-dim0-1])/ctl[dim-dim0])
        dim=dim+1
    E[0].append(E_n[0])
    E[1].append(E_n[1])
    E[2].append(E_n[2])
    v[0].append(v_n[0])
    v[1].append(v_n[1])
    v[2].append(v_n[2])
    return(E,v) 

x=np.arange(-10,10,0.01)
# def hermite(n,x):
#     if n==0:
#         H=np.ones(len(x))
#     elif n==1:
#         H=2*x
#     else:
#         H=2*x*hermite(n-1,x)-2*(n-1)*hermite(n-2,x)
#     return(H)



# D=[0.4,5]
# v=EvsD(D)[1]


# v0=v[0]
# v1=v[1]
# v2=v[2]

# phi_0=[0,0]
# phi_1=[0,0]
# phi_2=[0,0]


# n0=len(v0[0][0])
# n1=len(v0[1][0])


# for i in range(n0):
#     H_i=np.array(hermite(i,x))
#     phi_0[0]+=np.exp(-x*x/(2))*v0[0][0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
#     phi_1[0]+=np.exp(-x*x/(2))*v1[0][0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
#     phi_2[0]+=np.exp(-x*x/(2))*v2[0][0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
# for i in range(n1):
#     d_0=D[1]
#     H_i=np.array(hermite(i,x))
#     phi_0[1]+=np.exp(-x*x/(2))*v0[1][0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
#     phi_1[1]+=np.exp(-x*x/(2))*v1[1][0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))

# fig, ax=plt.subplots(2,1)
# ax[0].plot(x,phi_0[0])
# ax[1].plot(x,phi_0[1])
# plt.show()

# fig, ax=plt.subplots(2,1)
# ax[0].plot(x,phi_1[0])
# ax[1].plot(x,phi_1[1])
# plt.show()

# fig, ax=plt.subplots(2,1)
# ax[0].plot(x,phi_2[0])
# ax[1].plot(x,phi_2[1])
# plt.show()



# D=0.1 #6 #3
# E0=0 #+-5 #+-2.5
# v=E1vsD(D,E0)[1]
# v0=v[0]
# v1=v[1]
# v2=v[2]

# n0=len(v0[0])
# phi_0=[0]
# phi_1=[0]
# phi_2=[0]


# for i in range(n0):
#     #H_i=np.array(hermite(i,x))
#     H_i=np.array(hermite(i)(x))
    
#     phi_0[0]+=np.exp(-x*x/(2))*v0[0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
#     phi_1[0]+=np.exp(-x*x/(2))*v1[0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))
#     phi_2[0]+=np.exp(-x*x/(2))*v2[0][i]*H_i/((sqrt(sqrt(pi)*2**(i)*fact(i))))

# rho_0=phi_0[0]*phi_0[0]
# rho_1=phi_1[0]*phi_1[0]
# rho_2=phi_2[0]*phi_2[0]

# fig, ax=plt.subplots()
# ax.plot(x,phi_0[0])
# ax.plot(x,rho_0)
# fin=t.time()
# print(fin-inicio)
# plt.show()

# fig, ax=plt.subplots()
# ax.plot(x,phi_1[0])
# ax.plot(x,rho_1)
# plt.show()

# fig, ax=plt.subplots()
# ax.plot(x,phi_2[0])
# ax.plot(x,rho_2)
# plt.show()


# def simp(f,a,b):
#     n=len(f) #forzamos que n sea impar
#     h=(b-a)/n # notar que en realidad tenes n+1 puntos, es decir un número impar de puntos
#     I=0.0
#     j=1
#     while j<=n-2: #hay n/2 pares de intervalos
#         I+=(f[j+1]+f[j-1]+4*f[j])*h/3
#             #I=I*h/3
#         j+=2
#     return(I)


# I=simp(rho_0,-10,10)
# print(I)
