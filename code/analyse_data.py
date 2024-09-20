import matplotlib.pyplot as plt
import numpy as np

haut=[(206.33,241.41),(203.97,251.15),(204.31,263.84),(206.70,272.88),(212.03,279.71),(222.61,284.91),(232.22,290.63),(239.55,294.74),(249.78,297.58),(260.79,303.74),(274.38,305.33),(281.76,308.50),(293.87,311.43),(301.70,315.09),(310.87,310,37),(314.50,313,36),(325.13,317.62),(334.95,319.03),(353.73,320.41)]                          
alt=[(1471.76,1480.02,1491.53),(1471.8,1479.8,1490.47),(1471.69,1481.34,1489.87),(1471.05,1483.27,1488.63),(1468.6,1483.27,1488.31),(1470.75,1478.26,1488.12),(1475.95,1476.36,1485.98),(1479.3,1475.29,1485.35),(1477.41,1475.96,1485.24),(1474.47,1476.59,1485.26),(1478.56,1477.29,1486.13),(1480.5,1484.23,1489.44),(1484.48,1486.63,1491.67),(1487.09,1489.81,1493.79),(1489.6,1494.7,1495.66),(1491.55,1502.85,1501.45),(1498.02,1510.37,1505.37),(1502.78,1516.67,1516.06),(1512.61,1523.76,1517.99)]
bat=[(384.16,88.90),(386.55,97.93),(387.41,99.85),(389.87,107.48),(391.52,112.26),(395.26,112.90),(402.2,115.21),(406.97,123.89),(412.74,131.21),(418.29,133.36),(425.98,139.83),(430.75,148.51),(422.82,166.44),(429.40,166.76),(436.81,169.46),(439.14,179.90),(445.33,188.18),(451.13,204.89),(452.18,212.45)]


haut_x = [haut[i][0] for i in range(len(haut))]
haut_y = [haut[i][1] for i in range(len(haut))]
bat_x = [bat[i][0] for i in range(len(bat))]
bat_y = [bat[i][1] for i in range(len(bat))]
alt_m = [np.average(alt[i]) for i in range(len(alt))]
largeur=[np.sqrt((haut_x[i]-bat_x[i])**2+(haut_y[i]-bat_y[i])**2) for i in range(len(haut))]
pente = [np.arctan((alt_m[i]-alt_m[i+1])/(haut_x[i]-haut_x[i+1]))  for i in range(len(alt_m )-1)]
pente_tan = [np.tan(pente[i]) for i in range(len(pente))]

mu=0.39

def search_inf_mu():
    res=0
    i=0
    while True:
        if pente_tan[i] <= mu:
            res = i
            break
        i+=1
    return res

print(largeur[0])
    

plt.scatter(haut_x,haut_y)
plt.scatter(bat_x,bat_y)
plt.title("Topologie de la piste")
plt.xlabel("x")
plt.ylabel("y")
#plt.savefig("s1.png")
plt.show()

r=search_inf_mu()
t=[alt_m[r] for _ in range(len(alt_m))]
plt.scatter(haut_x,alt_m)
plt.plot(haut_x,t,c='red')
plt.title("Altitude de la piste en fonction de la distance")
plt.xlabel("distance en m")
plt.ylabel("altitude en m")
#plt.savefig("s2.png")
plt.show()



