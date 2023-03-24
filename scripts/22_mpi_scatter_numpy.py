# -*- coding: utf-8 -*-

from mpi4py import MPI
import numpy as np   
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

tamany=1000
bloc=tamany/size

# Al master creem un vector amb numpy. arrange el crea amb la serie 1,2,3,4,5...
# g_data --> global datat
if rank == 0:
   g_data =np.arange(tamany,dtype='i')
else:
    # als altres es cal la referència, encara que no continga res
   g_data = None

# Ara preparem el vector xicotet que contindrà la porció del gran.

# El creem buit mitjançant empty. 
# l_data --> local datat
l_data=np.empty(bloc,dtype='i')

# Fem la divisió. Dividim lo global a lo local
# Fixa't que la S és majúscula i conté una v al final (vector)
comm.Scatterv(g_data,l_data,root=0)

