from random import random
from math import sqrt

def pFactorSearch(start_value,end_value,composite_num): 
    pFactors = []
    while start_value<=end_value: 
        if composite_num%i==0:
            if esPrimer(i): 
                q=c/i
            pFactors.append(i)
            pFactors.append(q) 
        i=c+1
    else: 
        i+=1
    return pFactors


def esPrimer(i): 
    k=2
    while k<i:
        if (i%k==0):
            return False 
        else:
            k+=1 
    else:
        return True

# Calculo de pi pel mètode de montecarlo
# https://www.geogebra.org/m/cF7RwK3H

def piCalc(): 
    inside=0
    n=100000
    for i in range(0,n):
        #Creem dos numeros a l'atzar
        x=random() 
        y=random()
        #Si estan dins de la circumferència, contem
        if sqrt(x*x+y*y)<=1:
            #print(x,y,inside) 
            inside+=1
        
        # pi és la probabilitat de el punt haja caigut dins del cercle

    pi=4*inside/n 
    
    print('Han caigut %5d de %5d %.10f'%(inside,n,pi))
    return '%.10f'%(pi)


print(piCalc())