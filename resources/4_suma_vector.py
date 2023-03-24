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
   data = None

l_data=numpy.empty((bloc),dtype='i')
comm.Scatterv(data,l_data,root=0)
suma=0

for i in range(0,bloc):
	suma+=int(l_data[i])

#print ("Jo soc el procés %d i la meua suma és %d"%(rank,suma))

suma=comm.gather(suma,root=0)

if rank==0:
	print(suma)

	total=0

	for i in range(len(suma)):
		total+=suma[i]

	end=time.time()

	print("La suma total es %d, calculat en %3.6f"%(total,end-start))

