"""

This code computes pi. It's not the first python
pi computation tool that I've written.  This program
is a good test of the mpi4py library, which is
essentially a python wrapper to the C MPI library.

To execute this code:

mpiexec -np NUMBER_OF_PROCESSES -f NODES_FILE python mpipypi.py

where....

NUMBER_OF_PROCESSES is the number of desired processes.
NODES_FILE is a file which records the location of your nodes.

""" 

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

slice_size = 1000000
total_slices = 50

# A l'exemple tenim 16 processos i 50 trams que processar
# This is the master node.
if rank == 0:
    pi = 0
    slice = 0
    process = 1

    print size

    # Enviem la primera tanda de tasques. Aquest bucle es repetirà 16 cops
    # JA que hi han més trams que processos

    # tag=1 per a enviar dades
    # tag=2 per a enciar qui envia les dades
    while process < size and slice < total_slices:
        comm.send(slice, dest=process, tag=1)
        print "Sending slice",slice,"to process",process
        slice += 1
        process += 1

    # En aquest bucle es repetirà mentres no rebam 50 resposter de trams
    # Llavors quan es reb una resposta:
    #       tag=1 --> es guarda (acumula pi)          
    #       tag=2 --> mirem quin procés ens ha donat la resposta
    #           En cas de quedar més trams que computar
    #           Com eixe procés ha acabat, esta ociòs per a enviar-li una nova tasca

    received_processes = 0
    while received_processes < total_slices:
        # Esperem resposta de qualssevol node
        pi += comm.recv(source=MPI.ANY_SOURCE, tag=1)
        process = comm.recv(source=MPI.ANY_SOURCE, tag=2)
        print "Recieved data from process", process
        received_processes += 1

        if slice < total_slices:
            comm.send(slice, dest=process, tag=1)
            print "Sending slice",slice,"to process",process
            slice += 1

    # Matem els processos, ja que no tenim més feina que fer
    for process in range(1,size):
        comm.send(-1, dest=process, tag=1)

    # Mostrem els resultats i eixim del programa
    print "Pi is ", 4.0 * pi

# Ací tenim els treballadors. Tenen un rank>0
else:
    while True:     # Per sempre. Reben feina i donen resposta

        # Recepció. És bloqueja fins a rebre informació. Rebem del procés master (rank=0)
        start = comm.recv(source=0, tag=1)

        # Si rebem un -1 vol dir que acabem
        if start == -1: break

        #sinó hem acabat, calculem la nostra porció de la successió
        i = 0
        slice_value = 0
        while i < slice_size:
            if i%2 == 0:
                slice_value += 1.0 / (2*(start*slice_size+i)+1)
            else:
                slice_value -= 1.0 / (2*(start*slice_size+i)+1)
            i += 1

        # Enviem les dades (tag=1)
        comm.send(slice_value, dest=0, tag=1)
        # Enviem qui soc
        comm.send(rank, dest=0, tag=2)