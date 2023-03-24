# -*- coding: utf-8 -*-

from mpi4py import MPI
import sys

size=MPI.COMM_WORLD.Get_size()
rank=MPI.COMM_WORLD.Get_rank()
name=MPI.Get_processor_name()

print("Hello world, Soc el procés %2d de %d a %10s" %(rank,size,name))


