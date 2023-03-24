# -*- coding: utf-8 -*-


import numpy as np              # per treballar amb matrius
from mpi4py import MPI          # Per paralelitzar

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

tam=4 	# tamany del vector base dels nodes

# En tots els nodes. Creem el array
sendbuf = np.zeros(tam, dtype='i') + rank  # Un array de tam a valors el rank del node

print("Al node %d hem creat el array: "%rank,sendbuf)

# Creem una variable per a rebre les dades. Ha d'existir en tots els nodes
recvbuf = None

# Sols el node master fa reserva de memòria
if rank == 0:
	# La recepció és una matriu de tantes files com processos 
	# i tantes columnes com tamany te l'array
	# recvbuf = np.empty([size, tam], dtype='i')

	# La recepció és un array amb tantes caselles com
	# processos x tamany de l'array. Posarà un array a continuació de l'altre
	recvbuf = np.empty([size * tam], dtype='i')

# enviem la info i el node root la rep i la mostra
comm.Gather(sendbuf, recvbuf, root=0)
if rank==0:
	print recvbuf
