import numpy as np
import matplotlib.pyplot as plt

def p(c,amp):
    a=recherche_A(c,amp)
    xu=haut_x[a]-haut_x[c]
    Bp=(largeur[a]+largeur[c])/2 #largeur moyenne
    phi_a = np.arctan((alt_m[a]-alt_m[c])/xu) #angle de pente dans la zone d'écoulement à l'amont
    if phi_a <= np.arctan(mu) + (3.5 * np.pi/180):
        phi_a = np.arctan(mu) + (3.5 * np.pi/180)
    vp = ((Q / Bp) * epsi * (np.sin(phi_a) - mu * np.cos(phi_a))) ** (1/3) #vitesse en point P
    xu1 = xu / np.cos(phi_a) #longueur de la piste
    dp = Q / (Bp * vp) #épaisseur de neige au point P
    xu2 = 0.7 * (epsi / g) * dp
    if xu1 >= xu2 - xu2*0.1 and xu1 <= xu2 + xu2*0.1:
        return vp, dp
    else:
        p(c,50)
        
    
def recherche_A(c,amp):
    i=c+1
    while True:
        xu=haut_x[i]-haut_x[c]
        phi = np.arctan((alt_m[i]-alt_m[c])/xu) #angle de pente dans la zone d'écoulement à l'amont
        xu1 = xu / np.cos(phi) #longueur de la piste
        if xu1 >= 200-amp:
            break
        i+=1
    return i