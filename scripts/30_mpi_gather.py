from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# En tots els nodes, creem un valor distint en cadascun 1,4,9,16,..
data = (rank+1)**2

# Enviem tots a root les nostres dades simples

data = comm.gather(data, root=0)

if rank == 0:
	print "Les dades que he rebut son ", data

# Podem veure que no cal reserva de memòria de cap tipus
