# -*- coding: utf-8 -*-

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# El que envia té la informació
if rank == 0:
   data = 34;   #Pot-ser qualssevol tipus i valor
   # data={"nom":"Pepe","edat":43}
   # data= [3,4,5,6,7,8]
else:       # El que rep te sols la variable
    data = None

# -- Difussió --
data = comm.bcast(data, root=0)

# -- En totes el processos el mateix valor
print('Al node ' + str(rank) +':' )
print(data)