# -*- coding: utf-8 -*-
from mpi4py import MPI
import sys
import random

#   Ho fan tots. Quí soc i on estic ??

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status=MPI.Status()
name=MPI.Get_processor_name()

#           Codi de el master
if rank==0:
  for i in range(1,size):
    data=random.randint(1, 10)
    print("Soc root. Enviant %d al procés %d"%(data,i))
    comm.send(data,dest=i,tag=1)
  
  acabats=0
  while acabats<size:
    resposta=comm.recv(source=MPI.ANY_SOURCE,tag=1)
    proc=comm.recv(source=MPI.ANY_SOURCE,tag=2)
    print("El proces %d m'ha tornat un numero %d"%(proc,resposta))
    acabats=acabats+1

#            Codi dels nodes
else:
  my_data=comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
  tag=status.Get_tag()
  print("Soc %d i he rebut %d de root"%(rank,my_data))
  if tag==1: # datos
    x=my_data*rank
    comm.send(x,dest=0,tag=1)
    comm.send(rank,dest=0,tag=2)