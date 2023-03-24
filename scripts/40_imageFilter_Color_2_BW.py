# -*- coding: utf-8 -*-


from scipy import misc		# Carrega de imatges
from sys import argv		# per allegir arguments
import numpy as np		# per treballar amb matrius
from mpi4py import MPI		# Per paralelitzar
import time			# Per mesurar el temps
import os.path

def imprimirIMG(img):
	(fila,col,prof)=img.shape
	for i in range(fila):
		for j in range(col):
			print "[%3d,%3d,%3d] "%(img[i][j][0],img[i][j][1],img[i][j][2]),

		print("")


comm = MPI.COMM_WORLD		# DEFINE THE COMMUNICATOR
size = comm.Get_size()		# FIND THE SIZE OF THE COMMUNICATOR CLASS
rank = comm.Get_rank()		# FIND THE RANK OF THE CURRENT NODE
name = MPI.Get_processor_name()   # host


print("Proces %d de %d en %s en marxa"%(rank,size,name))
if rank==0:
	# Suposem tot be
	error=False

	if len(argv)!=2:
		print("Cal posar el nom de la imatge a processar")
        	error=True

	# verifiquem que existeix el fitxer
	nom_in=argv[1]
	if not os.path.isfile(nom_in):
		print("El fitxre %s no existeix. Eixint" %nom_in)
        	error=True

# seguim el master carrega la imatge
start = time.time()

if rank==0:
	# separem el nom del fitxer i la extensió
	(nom,ext)=os.path.splitext(nom_in)

	# generem el nom d'eixida
	nom_out=nom + "_bw" + ext

	# Càrrega de dades i distribució de les mateixes
	g_img = misc.imread(nom_in)

	# llegim dimensió de la imatge
	(g_rows,g_cols,colors)=g_img.shape
	print ("la imatge te %d-%d amb una profunditat de %d colors"%(g_rows,g_cols,colors))

	if g_rows % size != 0:
		print("L'alt de l'imatge es %d, que no es divisible per %d. Eixint "%(g_rows,size))
		error=True

	# calculem els fragments (tamany de la imatge que processara cada node)
	l_rows=int(g_rows/size)
	l_cols=g_cols

	#	print("Dividint una imatge de %dx%d entre %d es queda %dx%d"%(g_rows,g_cols,size,l_rows,l_cols))

	# Creem un array per a transferir les dimensions que te que processar cada node
	InArray = np.array([l_rows, l_cols,colors])
else:		# als nodes creem les variables buides per tenir les referències
	InArray =None
	g_img=None
	error=None

# Enviem a tots si hi ha error. Per a que puguen acabar
error=comm.bcast(error,root=0)

# Si hi ha un error acabem tots els programes
if error:
        quit()

# A partir d'aci tots tenen el mateix. S'envien les dimensions a tots els nodes
InArray = comm.bcast(InArray, root = 0)	 # El root = 0 o pare és qui ho executa

# Creem la imatge local amb la dimensió del que hem enviat.
l_rows=InArray[0]
l_cols=InArray[1]
colors=InArray[2]

# Aquesta serà la porció de la imatge a processar. Reservem memporia
# Fixa't que és tridimensional 
l_img=np.empty([l_rows,l_cols,colors],dtype='uint8')


# Dividim la imatge global en la menuda i enviem a tots els nodes
comm.Scatterv(g_img,l_img,root = 0)

# Tots els processos tenen la imatge en color per a processar-la

# Creem la nova imatge (de les dimensions locals i en blanc i negre
# Aquesta, com és en BN és bidimensional
l_img_out=np.empty([l_rows,l_cols],dtype='uint8')


#Creem la imatge en B/N 
for i in range(l_rows):
	for j in range(l_cols):
	# ( (0.3 * R) + (0.59 * G) + (0.11 * B) ).
		l_img_out[i][j]=int(0.3*l_img[i][j][0]+0.59*l_img[i][j][1]+0.11*l_img[i][j][2])


# preparem la variable per al retorn, Sols fem reserva en el master
g_img_out= None
if rank==0:
	# Mateixes dimensions que la original, però sols una dimensió (BN)
	g_img_out=np.empty([g_rows,g_cols],dtype='uint8')


# recuperem la imatge de retorn
comm.Gather(l_img_out,g_img_out,root=0)

# si som el node mestre la guardem a un fitxer
if rank==0:
#	print(g_img_out)
	misc.imsave(nom_out,g_img_out)
	end = time.time()
	print ("Imatge processada en %4.6f segons" %(end - start))
