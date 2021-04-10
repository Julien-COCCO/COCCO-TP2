# Appel des bibliothèques utiles
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc
#

##Definition de la fonction suspension(Y,t)

def suspension(Y,t): #Création de la fonction suspension(Y,t) qui renvoie Y'
    x1p = Y[2]
    x2p = Y[3]
    x3p = (1/M1)*(C2*Y[3]-C2*Y[2]-(K1+K2)*Y[0]+K2*Y[1])
    x4p = (1/M2)*(C2*Y[2]-C2*Y[3]+K2*Y[0]-K2*Y[1]+f)
    return(np.array([x1p,x2p,x3p,x4p]))

##Declaration des variables

tfin = 3
n = 100000

# Initialisation des constantes
M1 = 15
M2 = 200
C2 = 1200
K1 = 50000
K2 = 5000
f = -1000
#

t = np.linspace(0,tfin,n) # Création du vecteur temps

# Création d'un vecteur pour représenter l'état du système avant t = 0
ta = np.linspace(-1,0,10)
Ya = np.zeros(10)
#

##Résolution du Problème avec odeint

Y0 = np.array([0,0,0,0]) # Création du vecteur Y0
Yode = sc.odeint(suspension,Y0,t)

##Tracé

plt.plot(ta,Ya)
plt.plot(t,Yode[:,0],label="x1")
plt.plot(t,Yode[:,1],label="x2")
plt.xlabel("Temps t(s)")
plt.ylabel("Position x(m)")
plt.legend()
plt.show()