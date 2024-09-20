import numpy as np
import matplotlib.pyplot as plt

#!données
x=[(206.33,241.41),(203.97,251.15),(204.31,263.84),(206.70,272.88),(212.03,279.71),(222.61,284.91),(232.22,290.63),(239.55,294.74),(249.78,297.58),(260.79,303.74),
   (274.38,305.33),(281.76,308.50),(293.87,311.43),(301.70,315.09),(310.87,310,37),(314.50,313,36),(325.13,317.62),(334.95,319.03),(353.73,320.41),(378.34,327.69),
   (423.39,331.26),(458.10,334.33),(486.97,341.35),(514.76,351.14),(534.16,359.11),(560.12,367.87),(580.33,378.70),(618.12,396.01),(636.18,402.51),(652.0,406.55)]                          
alt=[(1471.76,1480.02,1491.53),(1471.8,1479.8,1490.47),(1471.69,1481.34,1489.87),(1471.05,1483.27,1488.63),(1468.6,1483.27,1488.31),(1470.75,1478.26,1488.12),
     (1475.95,1476.36,1485.98),(1479.3,1475.29,1485.35),(1477.41,1475.96,1485.24),(1474.47,1476.59,1485.26),(1478.56,1477.29,1486.13),(1480.5,1484.23,1489.44),
     (1484.48,1486.63,1491.67),(1487.09,1489.81,1493.79),(1489.6,1494.7,1495.66),(1491.55,1502.85,1501.45),(1498.02,1510.37,1505.37),(1502.78,1516.67,1516.06),
     (1512.61,1523.76,1517.99),(1528.16,1548.74,1539.47),(1559.79,1576.29,1553.55),(1581.49,1593.06,1588.67),(1602.08,1614.81,1619.49),(1623.89,1633.56,1642.55),
     (1639.27,1651.58,1658.95),(1663.26,1687.01,1671.61),(1689.06,1703.95,1693.73),(1741.61,1720.85,1720.16),(1755.46,1738.52,1749.21),(1786.45,1774.83,1778.1)]
y=[(384.16,88,90),(386.55,97.93),(387.41,99.85),(389.87,107.48),(391.52,112.26),(395.26,112.90),(402.2,115.21),(406.97,123.89),(412.74,131.21),(418.29,133.36),
   (425.98,139.83),(430.75,148.51),(422.82,166.44),(429.40,166.76),(436.81,169.46),(439.14,179.90),(445.33,188.18),(451.13,204.89),(452.18,212.45),(459.11,244.71),
   (474.84,260.49),(499.05,286.06),(519.74,296.45),(542.77,307.41),(565.51,314.61),(586.88,320.80),(607.24,328.35),(625.95,331.12),(647.86,335.93),(658.19,356.15)]

phi = 41 * (np.pi / 180) #angle pente départ
g = 9.81
epsi = 1000 #facteur de  frottement turbulent 
mu = 0.29 #coefficient frottement solide

#!traitement des données
x_x = [x[i][0] for i in range(len(x))]#traitement des coordonées
x_y = [x[i][1]  for i in range(len(x))]
y_x = [y[i][0]  for i in range(len(y))]
y_y = [y[i][1]  for i in range(len(y))]
alt_m = [np.average(alt[i]) for i in range(len(alt))]#altitude moyenne en chaque point
largeur=[np.sqrt((x_x[i]-y_x[i])**2+(x_y[i]-y_y[i])**2) for i in range(len(x))]#largeur entre les deux extrémités
pente = [np.arctan((alt_m[i]-alt_m[i+1])/(x_x[i]-x_x[i+1]))  for i in range(len(alt_m)-1)]#pente pour chaque point par rapport à l'horizontal
pente_tan = [np.tan(pente[i]) for i in range(len(pente))]#tengente de chaque angles



#!epaisseur de la neige
alt = alt_m[len(alt_m)-1] #altitude de départ
d0_period = 1.5 #epaisseur de neige de référence
d0_etoile = d0_period + (0.05 * (alt - 2000))/100#valeur de base
f_phi = 0.291 / (np.sin(phi) - 0.0202 * np.cos(phi)) #résistance de la neige
d0 = d0_etoile * f_phi #epaisseur de la neige
#augmenter de 30 a 50 com dans les zone de neige soufflée
#moins important de la correction dans les régions en xe haltitude

#!valeurs initiales
B0 = largeur[len(largeur)-1]  #plus grande largeur d ela zone de départ
v0 = np.sqrt(d0 * epsi * (np.sin(phi) - mu * np.cos(phi))) #vitesse à la sortie de la zone de déclenchement)
Q = B0 * d0 * v0 #vaguement rectangulaire

#!recherche du point P
#fonction qui permet de treuver le point A qui est au environ de 200m
#c le point tel que tan(theta) <= mu
def recherche_A(c,n):
    i=c+1
    while True:
        xu=x_x[i]-x_x[c]
        psi = np.arctan((alt_m[i]-alt_m[c])/xu) #angle de pente dans la zone d'écoulement à l'amont
        xu1 = xu / np.cos(psi) #longueur de la piste
        if xu1 >= 200-n:
            break
        i+=1
    return i

#fonction qui recherche l'angle psi_A et retourne vp et dp
def p(c,n):
    a=recherche_A(c,n)
    xu=x_x[a]-x_x[c]
    Bp=(largeur[a]+largeur[c])/2 #largeur moyenne
    psi_a = np.arctan((alt_m[a]-alt_m[c])/xu) #angle de pente dans la zone d'écoulement à l'amont
    if psi_a <= np.arctan(mu) + (3.5 * np.pi/180):
        psi_a = np.arctan(mu) + (3.5 * np.pi/180)
    vp = ((Q / Bp) * epsi * (np.sin(psi_a) - mu * np.cos(psi_a))) ** (1/3) #vitesse en point P
    xu1 = xu / np.cos(psi_a) #longueur de la piste
    dp = Q / (Bp * vp) #épaisseur de neige au point P
    xu2 = 0.7 * (epsi / g) * dp
    if xu1 >= xu2 - xu2*0.10 and xu1 <= xu2 + xu2*0.10:
        return vp, dp
    else:
        return p(c,10+n)
        
    

#recherche point critique tan(theta) = mu
def search_inf_mu():
    res=0
    i=0
    while True:
        if pente_tan[i] <= mu:
            res = i
            break
        i+=1
    return res

#!calculs distance arrêt et épaisseur final
def arret(dp, vp, phi_s):
    ds = dp + ((vp ** 2) / (10 *g))
    v2 = ds * epsi * (-np.sin(phi_s) + mu * np.cos(phi_s))
    s = (ds * epsi)/(2 * g) * np.log(1 + (vp ** 2) / (v2 ** 2))
    return (ds,s)


#!main
c=search_inf_mu()
print(B0,Q,d0,v0)
vp, dp = p(c,0)
print(vp,dp)
ds,s = arret(dp,vp,pente_tan[c-1])
print(ds,s)


#!pression
x_tot=[] #variables pour mettre les données
y_tot= []
z_tot=[]
dt=[]

#oblstacle important
rho = 300 #masse volumique neige 300Kg/m3
alpha = 0 #angle déviation
myu = 0.30 #contact neige/beton 

'''
#fonction qui calcule la pression pour une hauteur de mur de 0 à 6m et une inclinaison de 0 à 90deg
d=0
while d < 6:
    x =[]
    y = []
    z=[]
    dt.append(d)
    for a in range(0,91):
        alpha = (90-a) * (np.pi / 180)
        x.append(a)
        rho_n = rho * (vp ** 2) * np.sin(alpha) ** 2
        y.append(rho_n)
        if d < dp:
            z.append(myu * rho_n + rho * g * (dp - d) * np.cos(phi))
        else:
            z.append(myu * rho_n)
    x_tot.append(x)
    y_tot.append(y)
    z_tot.append(z)
    d+=0.5
for i in range(len(x_tot)):
    plt.plot(x_tot[i],y_tot[i])
    plt.plot(x_tot[i],z_tot[i])
    plt.title("Pression de la neige en fonction de l'inclinaison du mur d'hauteur: ")
    plt.xlabel("inclinaion du mur en degrée")
    plt.ylabel("pression exercée sur le mur en Pa")
    plt.legend(["force normale","force tangeantielle"])
    plt.savefig("fig2"+str(i))
    plt.show()
'''
#!cout
prix_m3 = 350
longueur=14
epaisseur=1.3
xp = []
yp = []
#fonction qui calcule le prix du mur en fonction de l'inclinaison
for i in range(0,60):
    v =(longueur / np.cos((i) * (np.pi / 180))) * epaisseur * prix_m3 *2
    xp.append(i)
    yp.append(v)
plt.plot(xp,yp)
plt.title("prix du mur")
plt.xlabel("inclinaion du mur en degrée")
plt.ylabel("prix en euro")
plt.savefig("fig_prix")
plt.show()


#!topographie
plt.scatter(x_x,x_y)
plt.scatter(y_x,y_y)
plt.title("Topologie de la piste")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("s1.png")
plt.show()

r=search_inf_mu()
t=[alt_m[r] for _ in range(len(alt_m))]
plt.scatter(x_x,alt_m)
plt.plot(x_x,t,c='red')
plt.title("Altitude de la piste en fonction de la distance")
plt.xlabel("distance en m")
plt.ylabel("altitude en m")
plt.savefig("s2.png")
plt.show()
