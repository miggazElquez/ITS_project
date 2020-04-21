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
 
def find_extremum2(tab, pas, x, y):
    while True:
        if tab[x][y]<tab[x+1][y]:
            x+=1
        elif tab[x][y]<tab[x-1][y]:
            x-=1
        elif tab[x][y]<tab[x][y+1]:
            y+=1
        elif tab[x][y]<tab[x][y-1]:
            y-=1
        else:
            break
    return (y*pas-10, x*pas-10)

# Fonction trouvant un extremum au sein du tableau
def find_extremum( tab, xmin, xmax, ymin, ymax, x, y):
   
    xx =x
    yy =y
    dx = 1
    dy = 1
 
    for i in range(200):
        if x < xmax and x > xmin and y < ymax and y > ymin:
            dx = tab[x+1][x-1]
            dy = tab[y+1][y-1]

            xx+= sign(dx)
            yy+= sign(dy)

    return (xx,yy)


# Nous definissons ici le tableau qui va contenir les valeurs pour chaque point (x,y)
xmin = -10
xmax = 10
ymin = -10
ymax = 10

pas = 0.1
nbx = int((xmax-xmin)/pas)
nby = int((ymax-ymin)/pas)
# Ici, le tableau est initialise
tableau = [[ 0.0 ]*nbx for j in range(nby)]


# Mise en place de l'ensemble contenant les extrema futurs pour x et y

extr = {*()}


# Mise en place des valeurs ainsi que des listes necessaires a la creation de multiples gaussienne 2-dimensionelles
nb_gaussiennes = 1
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


# Ici, on ajoute à l'ensemble des extrema en x et y des extrema generes a partir du tableau
#ex,ey = find_extremum(tableau, 0, nbx, 0, nby, 4, 4)
ex,ey = find_extremum2(tableau,pas,0,0);
extr.add((ex,ey))





# Finalement, matplotlib est employe dans le but d'afficher les resultats a l'ecran

# Le tableau de valeurs est dessine a l'ecran
plt.imshow(tableau, extent=[xmin, xmax, ymin, ymax], origin="lower", cmap='Blues_r', alpha=1)

# Mise en place d'une legende de couleurs
plt.colorbar()

# Affichage des extrema
for x_extr, y_extr in extr:
    plt.plot(x_extr, y_extr,'ro', label='extrema')

# Affichage des bassins d'attraction
#plt.imshow(tableau, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='RdGy', alpha=1.5)


# Executer Matplotlib
plt.legend()
plt.show()
