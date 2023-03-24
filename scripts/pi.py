import time
import math

slice_size = 1000000
print("%15s - %-20s - %-24s - %-24s" %("Termes calculats","Valor de pi","Error absolut","temps"))
for slices in range(1,100):


    termes=slice_size*slices
    #termes=1000000
    start = time.time()
    pi4=0.0
    i = 0
    while i < termes:
        if i%2 == 0:
            pi4 += 1.0 / (2*i+1)
        else:
            pi4 -= 1.0 / (2*i+1)
        i += 1


    end = time.time()
    pi=pi4*4;
    error = abs(pi - math.pi)
    print ("%15d - %.20f - %.24f - %4.6f" % (termes,pi,error,end - start))
