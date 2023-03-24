# -*- coding: utf-8 -*-

"""
Programa per veure el funcionament de l'enviament
Enviarà un vector a tots els processos. Cada process mostrara
La celda que lo correspon
"""
from mpi4py import MPI
import numpy
import sys
import time

def enum(*sequential, **named):
    """Handy way to fake an enumerated type in Python
    http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


def sumar(v,inici,fi):
	sum=0
	for i in range(inici,fi):
		sum+=int(v[i])
	return sum


# definim els canals de comunicació
tags = enum('DATA', 'PROC','END')

comm = MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
name=MPI.Get_processor_name()
status=MPI.Status()

tamany=int(sys.argv[1])
tros=tamany/size

start=time.time()
if rank==0:
	#master
	# Creem un vector de tamany elements
	data = numpy.arange(tamany, dtype='i')
	suma=0
	#send data to slaves
	for i in range(1,size):
		comm.Send([data,MPI.INT],dest=i,tag=tags.DATA)

	#Calcular la meua part
	suma+=sumar(data,rank*tros,(rank+1)*tros)

	#recieve data
	recieved=0
	while recieved<size-1:
		x_rec=comm.recv(source=MPI.ANY_SOURCE,tag=tags.DATA)
		proc=comm.recv(source=MPI.ANY_SOURCE,tag=tags.PROC)
		print("El procés %d em retonra un %d"%(proc,x_rec))
		suma+=x_rec
		recieved+=1

	# acabem els treballadors
	for i in range(1,size):
		comm.send(None,dest=i,tag=tags.END)

	end=time.time()
	print("La suma total es %d, calculada en %4.6f"%(suma,end-start))
else:
	#slave
	while True:
		my_data = numpy.empty(tamany, dtype='i')
		comm.Recv([my_data,MPI.INT],source=0,tag=MPI.ANY_TAG,status=status)
		tag=status.Get_tag()
		if tag==tags.DATA:
			# WORK
			x=sumar(my_data,rank*tros,(rank+1)*tros)
			comm.send(x,dest=0,tag=tags.DATA)
			comm.send(rank,dest=0,tag=tags.PROC)
		elif tag==tags.END:
			break




