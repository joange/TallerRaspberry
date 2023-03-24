# -*- coding: utf-8 -*-

"""
Programa per veure el funcionament de l'enviament
Enviarà un vector a tots els processos. Cada process mostrara
La celda que lo correspon
"""
from mpi4py import MPI
import sys

def enum(*sequential, **named):
    """Handy way to fake an enumerated type in Python
    http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# definim els canals de comunicació
tags = enum('DATA', 'PROC','END')

comm = MPI.COMM_WORLD
size=comm.Get_size()
rank=comm.Get_rank()
name=MPI.Get_processor_name()
status=MPI.Status()

data=[1.0,2.0,3.0,4.0]

if rank==0:
	#master
	#send data
	for i in range(1,size):
		comm.send(data,dest=i,tag=tags.DATA)

	#recieve data
	recieved=0
	while recieved<size-1:
		x_rec=comm.recv(source=MPI.ANY_SOURCE,tag=tags.DATA)
		proc=comm.recv(source=MPI.ANY_SOURCE,tag=tags.PROC)
		print("El procés %d em retonra un %d"%(proc,x_rec))
		recieved+=1

	# acabem els treballadors
	for i in range(1,size):
		comm.send(None,dest=i,tag=tags.END)
else:
	#slave
	while True:
		my_data=comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
		tag=status.Get_tag()
		if tag==tags.DATA:
			# WORK
			x=10*my_data[rank]
			comm.send(x,dest=0,tag=tags.DATA)
			comm.send(rank,dest=0,tag=tags.PROC)
		elif tag==tags.END:
			break




