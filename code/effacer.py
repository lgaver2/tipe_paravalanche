lamb = 0 #plus grande distance parcouruepar un petit volume de neige
vm = v0 #meme formule mais calc sur lambda
dt = lamb / vm #temps d'écoulement moyen
#22

#Rp = 0#rayon hydraulique dans la zone d'écoulement
#vp = np.roots(Rp * epsi * (np.sin(phi) - mu * np.cos(phi)))
#Bp = (Q / vp ** 3) * epsi * (np.sin(phi) - mu * np.cos(phi)) #largeur avalanche en P
#dp =  Q / (Bp * vp)
#xu2 = 0.7 * (epsi / g) * dp


#todo effort exercer
#oblstacle important
#rho = 300 #masse volumique neige 300Kg/m3
#alpha = 30 * (np.pi / 180) #angle déviation
#rho_n = rho * (v ** 2) * np.sin(alpha) ** 2 #pression statiionaire normale à la surface de l'obstacle
#rho_s = mu * rho_n #contrainte tangentielle avec rho_n + Pneige( rho * g * d * cos phi) si dépasse l'obstacle
#si contact mur / béton mu = 0.30
#dtot = dp + (vp ** 2) / (2*g*lamb)#av lambda = 1.5: neige légère et seiche, 2 à 3 neige lourde
#24

#rho_n = rho * (v ** 2) * np.sin(alpha) ** 2 #pression statiionaire normale à la surface de l'obstacle
#rho_s = myu * rho_n #contrainte tangentielle avec rho_n + Pneige( rho * g * d * cos phi) si dépasse l'obstacle
#si contact mur / béton mu = 0.30
'''for alpha in range(0, 15):
    x1=[]
    x2=[]
    x3=[]
    x.append(alpha)
    for d in range(1,5):
        x1.append(d)
        rho_n = rho * (vp ** 2) * np.sin(alpha) ** 2
        x2.append(rho_n)
        if d < dp:
            x3.append(myu * rho_n + rho * g * (dp - d) * np.cos(phi))
        else:
            x3.append(myu * rho_n)
    y.append([x1,x2,x3])

for i in range(len(x) - 1):
    plt.plot(y[i][0], y[i][1])
    plt.plot(y[i][0], y[i][2])
    plt.title("angle"+str(x[i]))
    print()
    plt.show()'''
#66


