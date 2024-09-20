import numpy as np
import random as rd
import matplotlib.pyplot as plt
import os
import glob

def initialize_random_tab(tab,s):
    for i in range(s):
        for j in range(s):
            tab[i][j] = rd.randrange(0,5)

def ebouler(tab,i,j,s):
    if i >= 1:
        tab[i-1][j] += 1
    if i <= s-2:
        tab[i+1][j] += 1
    if j >= 1:
        tab[i][j-1] += 1
    if j <= s-2:
        tab[i][j+1] += 1

def avalanche(tab,s):
    equilibre = False
    step = 0
    while(not equilibre):
        equilibre = True
        for i in range(s):
            for j in range(s):
                if tab[i][j] >= 4:
                    tab[i][j] -= 4
                    ebouler(tab,i,j,s)
                    equilibre = False
                    step += 1
                    plt.figure()
                    plt.imshow(tab)
                    plt.title("step"+str(step))
                    plt.colorbar()
                    plt.savefig("D:\Documents\TIPE\TIPE\\avalanche-code\img\step"+str(step)+".png")
    return step


img_folder = "D:\Documents\TIPE\TIPE\\avalanche-code\img"   
#enlever les fichier images
res=glob.glob(f"{img_folder}/*.png")
for img in res:
    os.remove(img)

rd.seed(1)
size = 3
#tab = np.zeros((size,size))
#initialize_random_tab(tab,size)
tab=[[4,4,4],[3,-1,2],[-1,0,-1]]
#tab += id
#tab = np.ones((size,size)) * 4
print(tab)
step=avalanche(tab,size)
print(tab)
print(step)
