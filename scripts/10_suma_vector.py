# -*- coding: utf-8 -*-

"""
Programa que suma un vector, per comparar els temps.
Es crea un vector aleatori d'un tamany concret
Es sumen les seues caselles i es mostra per pantalla
"""
import numpy
import time
import sys

def sumar(v,inici,fi):
	sum=0
	for i in range(inici,fi):
		sum+=int(v[i])
	return sum

tamany=int(sys.argv[1])

suma=0
start=time.time()
data = numpy.arange(tamany, dtype='i')
suma=sumar(data,0,tamany)
end=time.time()
print("La suma total es %d, calculat en %3.4f"%(suma,end-start))