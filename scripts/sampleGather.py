import numpy
from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
root = 0

a_size = 4
recvdata = None
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.float64)

if rank == 0:
   recvdata = numpy.arange(size*a_size,dtype=numpy.float64)

comm.Gather(senddata,recvdata,root=0)
print 'on task',rank,'after Gather:    data = ',recvdata 

counts=(2,3,4)
dspls=(0,3,8)
if rank == 0:
   recvdata = numpy.empty(12,dtype=numpy.float64)
sendbuf = [senddata,counts[rank]]
recvbuf = [recvdata,counts,dspls,MPI.DOUBLE]
comm.Gatherv(sendbuf,recvbuf,root=0)
print 'on task',rank,'after Gatherv:    data = ',recvdata

"""

local_array = [rank] * random.randint(2, 5)
print("rank: {}, local_array: {}".format(rank, local_array))

sendbuf = np.array(local_array)
#print("local",local_array)
#print("send",sendbuf)
# Collect local array sizes using the high-level mpi4py gather
sendcounts = np.array(comm.gather(len(sendbuf), root))

if rank == root:
    print("sendcounts: {}, total: {}".format(sendcounts, sum(sendcounts)))
    recvbuf = np.empty(sum(sendcounts), dtype=int)
else:
    recvbuf = None

comm.Gatherv(sendbuf=sendbuf, recvbuf=(recvbuf), root=root)
#comm.Gatherv(sendbuf=sendbuf, recvbuf=(recvbuf, sendcounts), root=root)
if rank == root:
    print("Gathered array: {}".format(recvbuf))
"""
