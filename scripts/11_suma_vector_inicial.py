# -*- coding: utf-8 -*-

from mpi4py import MPI
import numpy
import sys
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

tamany=int(sys.argv[1])
bloc=tamany/size

start=time.time()

if rank == 0:
   data =numpy.arange(tamany,dtype='i')
else:
   data = None # Molt important. data ha d'estar inicialitzat

data=comm.bcast(data,root=0)


inici=rank*bloc
final=(rank+1)*bloc
suma=0
for i in range(inici,final):
	suma+=int(data[i])

if rank==0:
	total=suma #la meua suma
	for i in range(size-1):
		parcial=comm.recv(source=MPI.ANY_SOURCE,tag=1)
		total+=parcial
	end=time.time()
	print("La suma del vector es %d calculat en %2.5f"%(total,end-start))
else:
	comm.send(suma,dest=0,tag=1)
