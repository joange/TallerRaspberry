# -*- coding: utf-8 -*-

import numpy as np              # per treballar amb matrius
from mpi4py import MPI          # Per paralelitzar

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

tam=4
# creem una matriu quadrada. Amb valor inicial el rank del procés
sendbuf = np.zeros([tam,tam], dtype='i') + rank

print("El proces %d ha creat: "%rank,sendbuf)

# creem varaible en tots els nodes
recvbuf = None

# sols el master contindrà la recepció dels valors
# fem la reserva de memòria
if rank == 0:
	# opció 1. Una matriu damunt de l'altra
	# recvbuf = np.empty([tam*size, tam], dtype='i')

	# opció 2. Cada matriu d'orige a un vector. Cada fila serà un procés
	# recvbuf = np.empty([tam, tam*size], dtype='i')

	# opció 3 De totes les matrius a un sol vector
	recvbuf = np.empty([tam*tam*size], dtype='i')


# tots envien les dades al root
comm.Gather(sendbuf, recvbuf, root=0)

# mostrem la matriu
if rank==0:
	print recvbuf
