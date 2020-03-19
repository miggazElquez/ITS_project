from math import *
from random import randint, random, uniform
from pprint import pprint
import matplotlib.pyplot as plt

def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

def gaussienne_2d(x, y, mx, my, sx, sy):
    a = 1 / ( 2 * pi * sx * sy )
    #a = 1
    b = (-1/2) *( ( (x-mx)/sx )**2 + ( (y-my)/sy )**2 )
    #b = -( ( (x-mx)/sx )**2 + ( (y-my)/sy )**2 )
    return a * exp(b)

def find_extremum( tab, x, y):
    return (x,y)

#defining the value grid
xmin = -10
xmax = 10
ymin = -10
ymax = 10
pas = 0.1
nbx = int((xmax-xmin)/pas)
nby = int((ymax-ymin)/pas)
#define value table
tableau = [[ 0.0 ]*nbx for j in range(nby)]
x_extr = []
y_extr = []
#number of generated gaussian curves
nb_gaussiennes = 1
mx = [ randint(xmin,xmax)/2 for i in range(nb_gaussiennes) ]
my = [ randint(ymin,ymax)/2 for i in range(nb_gaussiennes) ]
sxmin=4.0
symin=4.0
sxmax=4.0
symax=4.0
sx = [ uniform(sxmin,sxmax) for i in range(nb_gaussiennes) ]
sy = [ uniform(symin,symax) for i in range(nb_gaussiennes) ]




#loop through the value grid for each generated standard deviation and average and apply the corresponding gaussian function
for k in range(nb_gaussiennes):
    for i in range(nbx):
        for j in range(nby):
            #print(f"{xmin+i*pas},{ymin + j*pas} : {gaussienne_2d( xmin+i*pas, ymin + j*pas, mx[k], my[k], sx[k], sy[k])}")
            tableau[i][j] += gaussienne_2d( xmin+i*pas, ymin + j*pas, mx[k], my[k], sx[k], sy[k] )


ex,ey = find_extremum(tableau, 0, 0)
x_extr.append(ex)
y_extr.append(ey)

#draw the value grid to the screen
plt.imshow(tableau, extent=[xmin, xmax, ymin, ymax], origin="lower", cmap='Blues_r', alpha=1)

#add a colorbar so one understands the meaning of the colors
plt.colorbar()

#plot extrema
plt.plot(x_extr, y_extr,'ro', label='extrema')


#draw the second value grid on which the attraction bassins are described
#plt.imshow(tableau, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='RdGy', alpha=1.5)

#show legends
plt.legend()
#show plot
plt.show()
