from math import *
from random import randint, random, uniform
from pprint import pprint
import matplotlib.pyplot as plt

# Utility function
def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

# Fonction generatrice de gaussiennes 2-dimensionelles
def gaussienne_2d(x, y, mx, my, sx, sy):
    a = 1 / ( 2 * pi * sx * sy )
    #a = 1
    b = (-1/2) *( ( (x-mx)/sx )**2 + ( (y-my)/sy )**2 )
    #b = -( ( (x-mx)/sx )**2 + ( (y-my)/sy )**2 )
    return a * exp(b)
 
# Fonction trouvant un extremum au sein du tableau
def find_extremum(tab, pas, x, y):
    x_max = len(tab) - 1
    y_max = len(tab[0]) - 1
    while True:
        if x < x_max and tab[x][y]<tab[x+1][y]:
            x+=1
        elif x > 0 and tab[x][y]<tab[x-1][y]:
            x-=1
        elif y < y_max and tab[x][y]<tab[x][y+1]:
            y+=1
        elif y > 0 and tab[x][y]<tab[x][y-1]:
            y-=1
        else:
            break
    return (y*pas-10, x*pas-10)

# Fonction trouvant un extremum au sein du tableau avec un nb maximum d'iteration possibles
def find_extremum_iter(tab, pas, x, y):
    max_iter = 20
    i = 0
    x_max = len(tab) - 1
    y_max = len(tab[0]) - 1
    while True:
        if i == max_iter:
            break
        if x < x_max and tab[x][y]<tab[x+1][y]:
            x+=1
        elif x > 0 and tab[x][y]<tab[x-1][y]:
            x-=1
        elif y < y_max and tab[x][y]<tab[x][y+1]:
            y+=1
        elif y > 0 and tab[x][y]<tab[x][y-1]:
            y-=1
        else:
            break
        i+=1
    return (y*pas-10, x*pas-10)

# Nous definissons ici le tableau qui va contenir les valeurs pour chaque point (x,y)
xmin = -10
xmax = 10
ymin = -10
ymax = 10

pas = 0.2
nbx = int((xmax-xmin)/pas)
nby = int((ymax-ymin)/pas)
# Ici, le tableau est initialise
tableau = [[ 0.0 ]*nbx for j in range(nby)]

# On initialise egalement un tableau de meme dimensions dans le but d'y placer les points appartenant aux bassins d'attractions
bassins = [[ 0.0 ]*nbx for j in range(nby)]

# Mise en place de l'ensemble contenant les extrema futurs pour x et y
x_extr = []
y_extr = []

# Mise en place des valeurs ainsi que des listes necessaires a la creation de multiples gaussienne 2-dimensionelles
nb_gaussiennes = 8
# Creation de positions aleatoires de gaussiennes
mx = [ randint(xmin,xmax)/2 for i in range(nb_gaussiennes) ]
my = [ randint(ymin,ymax)/2 for i in range(nb_gaussiennes) ]
# Definition et creation de leurs amplitudes respectives en x et en y
sxmin=1.0
symin=1.0
sxmax=3.0
symax=3.0
sx = [ uniform(sxmin,sxmax) for i in range(nb_gaussiennes) ]
sy = [ uniform(symin,symax) for i in range(nb_gaussiennes) ]


# Placement des valeurs generees par les gaussiennes dans le tableau de valeurs
for k in range(nb_gaussiennes):
    for i in range(nbx):
        for j in range(nby):
            #print(f"{xmin+i*pas},{ymin + j*pas} : {gaussienne_2d( xmin+i*pas, ymin + j*pas, mx[k], my[k], sx[k], sy[k])}")
            tableau[i][j] += gaussienne_2d( xmin+i*pas, ymin + j*pas, mx[k], my[k], sx[k], sy[k] )


# Ici, on ajoute au dictionnaire des extrema en x et y des extrema generes a partir du tableau
for i in range(nbx):
    for j in range(nby):
        ex,ey = find_extremum(tableau,pas,i,j)
        x_extr.append(ex)
        y_extr.append(ey)

for i in range(nbx):
    for j in range(nby):
        val = 0
        ex,ey = find_extremum_iter(tableau,pas,i,j)
        for k in range(len(x_extr)):
            if abs(x_extr[k] - ex)<0.00001  and abs(y_extr[k] - ey)<0.00001:
                val = 100 * (k+1)
                break
        bassins[i][j] = val

# Finalement, matplotlib est employe dans le but d'afficher les resultats a l'ecran

# Le tableau de valeurs est dessine a l'ecran
plt.imshow(tableau, extent=[xmin, xmax, ymin, ymax], origin="lower", cmap='Blues_r', alpha=1)

# Mise en place d'une legende de couleurs
plt.colorbar()

# Affichage des extrema
plt.plot(x_extr, y_extr,'ro', label='extrema')

# Affichage des bassins d'attraction
plt.imshow(bassins, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='gray', alpha=1.5)


# Executer Matplotlib
plt.legend()
plt.show()
