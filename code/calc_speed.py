import numpy as np

phi = 30 #angle pente
g = 9.81

#epaisseur de la neige
alt = 2000
d0_etoile = 0.88 + (0.05 * (alt - 2000))/100#valeur de base
f_phi = 0.291 / (np.sin(phi) - 0.020 * np.cos(phi)) #résistance de la neige
d0 = d0_etoile * f_phi #epaisseur de la neige
#augmenter de 30 a 50 com dans les zone de neige soufflée
#moins important de la correction dans les régions en haute haltitude

#débit
B0 = 0  #plus grande largeur d ela zone de départ
epsi = 0 #facteur de  frottement turbulent #!page 20 - 21
mu = 0 #coefficient frottement solide
v0 = np.roots(d0 * epsi * (np.sin(phi) - mu * np.cos(phi))) #vitesse à la sortie de la zone de déclenchement)
K = 0 #vomue de neige engagé dans l'avalanche
lamb = 0 #plus grande distance parcouruepar un petit volume de neige
vm = v0 #meme formule mais calc sur lambda
dt = lamb / vm #temps d'écoulement moyen
Q = B0 * d0 * v0 #vaguement rectangulaire
Q = K * dt #forme quelconque

#vitesse dt hauteur dans la zone d'écoulement
B = 0 #largeur avalanche
v = ((Q / B) * epsi * (np.sin(phi) - mu * np.cos(phi))) ** 1/3
d = Q / B * v


F = 0#section mouillée
U = 0 #périmètre mouillée
R = F / U #rayon hydorlique
v= np.roots(R * epsi * (np.sin(phi) - mu * np.cos(phi)))

#vitesse et hauteur
mu = np.tan(phi)

#vitesse ecoulement en P

phi_p = 0 #angle de pente dans la zone d'écoulement à l'amont
Rp = 0#rayon hydraulique dans la zone d'écoulement
vp = np.roots(Rp * epsi * (np.sin(phi) - mu * np.cos(phi)))
Bp = (Q / vp ** 3) * epsi * (np.sin(phi) - mu * np.cos(phi)) #largeur avalanche en P
dp = Q/ (Bp * vp)

#changement de pente
d2 = 0
xu = 0.7 * (epsi / g) * d2
#! 14- 15

#zone de dépot
ds = dp + (vp ** 2) / (10 * g)
v = np.roots(ds * epsi * (-1 * np.sin(phi) + mu * np.cos(phi)))
s = ((ds * epsi) / (2 *g)) * np.log(1+ (vp ** 2) + (v ** 2)) #distance d'arret

#todo effort exercer
#oblstacle important
rho = 0 #masse volumique neige 300Kg/m3
alpha = 0 #angle déviation
rho_n = rho * (v ** 2) * np.sin(alpha) ** 2 #pression statiionaire normale à la surface de l'obstacle
rho_s = mu * rho_n #contrainte tangentielle avec rho_n + Pneige( rho * g * d * cos phi) si dépasse l'obstacle
#si contact mur / béton mu = 0.30

#effort petit obstacle
F = 0 #surface de la projection de l'obstacle sur le plan perpendiculaire à la vitesse
c = 0 # coefficient résistance
P = c * F * (rho * (v ** 2)) /2 #résultante des efforts

dtot = d + (v ** 2) / (2 * g * lamb) #hauteur scolicité