import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

##Definition de la fonction pendule(Y,t)

def pendule(Y,t):
    return(np.array([Y[1],(-g/L)*np.sin(Y[0])]))

##Declaration des variables

g = 9.81
L = 1
tfin = 5
n = 100000
h = tfin/n
theta0 = np.pi/2

t = np.linspace(0,tfin,n)

##Problème linéarisé

Y = np.zeros(n)

for i in range(n):
    Y[i] = theta0*np.cos(np.sqrt(g/L)*t[i])

##Problème avec Euler

Y0 = np.array([theta0,0])
Ye = np.zeros((n,2))

Ye[0][:] = Y0

for i in range(1,n):
    Ye[i][:] = Ye[i-1][:] + h*pendule(Ye[i-1][:],i-1)

##Problème avec Range-Kutta ordre 4

Y0 = np.array([theta0,0])
Yrk = np.zeros((n,2))

Yrk[0][:] = Y0

k1 = np.zeros(2)
k2 = np.zeros(2)
k3 = np.zeros(2)
k4 = np.zeros(2)

for i in range(1,n):
    k1 = pendule(Yrk[i-1],i-1)
    k2 = Yrk[i-1][:] + (h/2)*k1
    k2 = pendule(k2,i-1)
    k3 = Yrk[i-1][:] + (h/2)*k2
    k3 = pendule(k3,i-1)
    k4 = Yrk[i-1][:] + h*k3
    k4 = pendule(k4,i-1)

    Yrk[i][:] = Yrk[i-1][:] + (h/6)*(k1+2*k2+2*k3+k4)

##Problème avec odeint

Y0 = np.array([theta0,0])
Yode = sc.odeint(pendule,Y0,t)

##Tracés

plt.plot(t,Y,label="Linéarisé")
plt.plot(t,Ye[:,0],label="Euler")
plt.plot(t,Yrk[:,0],label="Range-Kutta d'ordre 4")
plt.plot(t,Yode[:,0],label="odeint")
plt.xlabel("Temps t(s)")
plt.ylabel("Angle theta(rad)")
plt.legend()
plt.show()


