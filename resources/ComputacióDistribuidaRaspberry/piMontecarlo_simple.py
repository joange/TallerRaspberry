
from random import random
from math import sqrt,pi
import numpy as np



# Calculo de pi pel mètode de montecarlo
# https://www.geogebra.org/m/cF7RwK3H
inside=0
n=1000000
for i in range(0,n):
    #Creem dos numeros a l'atzar
    x=random() 
    y=random()
    #Si estan dins de la circumferència, contem
    if sqrt(x*x+y*y)<=1:
        inside+=1
    
    # pi és la probabilitat de el punt haja caigut dins del cercle

pi_calc=4*inside/n 

print('Han caigut %5d de %5d %.10f'%(inside,n,pi))
print('Valor calculat  %.80f'%(pi_calc))
print('Valor real      %.80f'%(pi))
print('Valor NumPy     %.80f'%(np.pi))