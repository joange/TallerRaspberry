# Imports
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size() 
rank = comm.Get_rank()

rows = 4
num_columns = rows/size

data=None

if rank == 0:
  data = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

recvbuf = np.empty((rows, int(num_columns)), dtype='int')
comm.Scatterv(data, recvbuf, root=0)
print('Rank: ',rank, ', recvbuf received:\n ',recvbuf)
