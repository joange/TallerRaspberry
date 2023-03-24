# -*- coding: utf-8 -*-

from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    # crea el vector [1,4,9,16] de quadrats
   data = [(i+1)**2 for i in range(size)]
else:
   data = None

# repartim les dades
data = comm.scatter(data, root=0)

# esperem una mica tots, de manera proporcional
time.sleep(rank/500)
print("Jo soc el procés %d i les meues dades son"%rank)
print(data)
