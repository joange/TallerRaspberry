# Muntatge i configuració d'un clúster de RaspberryPi amb computació distribuïda

## Materials

- 4 x Raspberry Pi
- 1 x Switch 100
- 4 x latiguillos
- Alimentadors i microSD
- Rack

## Muntatge del clúster

Enrackarem les Rpi de manera adient
Descarregar el Raspbian en una microSD.
Arrancar-la i instalar tot el SW que li cal (Python, MPI4PI i SSH). 

1. Arranquem amb la microSD que hem gravat al pas anterior. Li hem de connectar un teclat/monitor per pre-configurar-la

2. Executem `sudo raspi-config`:
   1. `Expand filesystem`  
   2. `Generar el locale` i configurar el teclat
   3. `Boot Options -> B2` Entrada en consola automàtica amb usuari `pi`
   4. `Advanced options`  -> hostname `node1`
   5. `Advanced options` ->  Memòria de GPU a 16MB
   6.  `Interfacing options` -> Instalar servidor SSH
   7.  Select "2. Network options". Select "N3 Network interface names". Select "No". It's now disabled predictable network interface names.
   8.  reiniciar


3. Accedim a la SD pre-configurada mitjançant SSH
   1. `sudo apt update` (no cal fer upgrade)
   2. Instalar MPICH:
      1. `mkdir mpich3` La carpeta que contindrà l'instalador
      2. `cd mpich3` Entrem
      3. `wget http://www.mpich.org/static/downloads/3.3.2/mpich-3.3.2.tar.gz` (o la versió estable). Descarreguem
      4. `tar xfz mpich-3.3.2.tar.gz` Descomprimim
      5.  `sudo mkdir /home/rpimpi`
      6.  `sudo mkdir /home/rpimpi/mpi-install`
      7.  `sudo mkdir /home/pi/mpi-build`
      8.  `cd /home/pi/mpi-build`
      9.  `sudo apt-get install gfortran`
      10. Comprovació de totes les llibreries necessàries ( 7 minuts aproximadament)
      11. `sudo /home/pi/mpich3/mpich-3.2.2/configure -prefix=/home/rpimpi/mpi-install`
      12. (pcompilem)
      13. `sudo make`
      14. (instalem)
      15. `sudo make install`
      16. afegim mpi al path: `nano .bashrc` en l'ultima linia `PATH=$PATH:/home/rpimpi/mpi-install/bin`
      17. reiniciar
  1. 
      1.  comprovar que mpi funciona: `mpiexec -n 1 hostname`
      2.  instalar les llibreries de desenvolupamnet de python `sudo apt install python-dev`
      3.  Instalar el gestor de llibreries `sudo apt install python-pip`
      4.  Instalar mpi4py `pip install mpi4py`

      `mpiexec -n 4 python helloworld.py`


Crear una img a partir de la microSD. 
Fregir-la en totes les altres raspberrys

<!--

      1.  Download mpi4py tarball.
      2.  
```
wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-2.0.0.tar.gz

actualment 3.0.3

Update.

sudo apt-get update --fix-missing

Unzip the file.

tar zxf mpi4py-2.0.0.tar.gz

Open the directory.sudo

cd mpi4py-2.0.0

Installation for Python3

sudo apt-get install python3-dev

sudo python3 setup.py build --mpicc=/home/rpimpi/mpi-install/bin/mpicc

sudo python3 setup.py install

Installation for Python

sudo apt-get install python-dev

sudo python setup.py build --mpicc=/home/pi/mpich-install/bin/mpicc

sudo python setup.py install
```

19. Afegir variable d'entorn al PATH `export PYTHONPATH=/home/pi/mpi4py-xx`  
20. Provar mpi4py en 1 node: `mpi4py` `mpiexec -n 5 python helloworld.py`

-->

- Clonar aquesta SD per fer la resta. Donar-li com a nom `imatgeCluster`
  - En windows <https://sourceforge.net/projects/win32diskimager/>
  - En mac <https://www.tweaking4all.com/hardware/raspberry-pi/applepi-baker-v2/#DownloadApplePiBaker>
  - En Linux
  - 
- Gravar-la en les altres 3 microSD (nodes 2, 3 i 4)


## Configuració de la xarxa

Arrancar el cluster. La xarxa de cada màquina està per DHCP. Amb un sniffer trobar les màquines i posra-los del IP que tindràn

Editar `/etc/dhcpd.conf` i assignar IP's estàtiques

afegir 

```bash
nohock lookup-hostname

interface eth0
static ip_address=192.168.10.11/24          # 11, 12, 13 i 14 respect
static routers=192.168.10.1
static domain_name_servers=192.168.10.1
```

Desde `sudo raspi-config` canviar el hostname a node2, node3 i node4 respectivament

reiniciar els nodes

editar el `/etc/hosts` de tots els nodes per a contenir les adreces i noms de tots els nodes

Comprovar-hoi amb pings si es veuen


## Proves d'execució

crear directori `mpi_test`
crear fitxer _machinefiles_. En ell hi han linies amb la següent estructura `maquina[:cores]`. Per exemple:

```
node1       # sols te un core
node2:2     # amb dos cores
node3:2     # amb dos cores
node4:4     # amb 4 cores
```

provem amb `mpiexec -f machinefile -n 4 hostname`

Fallará. El `node1` que és el master deu autenticarse amb els altres nodes automàticament. Per això necessitem afegir les claus ssh

### Afegir claus ssh 

- (en node1) `ssh-keygen`
- (en node1) `cd ~/-.ssh`
- (en node1) `cp id_rsa.pub node1_key`
- (en node1) `ssh pi@altreNode`
  
(repetir en tots els nodes)

- (en altreNode) `ssh-keygen`
- (en altreNode) `cd ~/-.ssh`
- (en altreNode) `cp id_rsa.pub altre_key`
- (en altreNode) `scp node1:/home/pi/.ssh/node1_key .`
- (en altreNode) `cat node1_key>>authorized_keys` 

(portar a node1 els certificats de la resta de nodes també)

## El programa a executar ha d'estar en tots els nodes del clúster

Això implica que si modifique alguna cosa, hem de portar dita modificació a totes les màquines.

### Solució:

Instalem nfs i muntem una carpeta en xarxa, de manera que en dita carpeta podrem guardar els nostres programes i per tant si ho modifiquen des d'un node, la modificació és extensible a tots els nodes:

- (en node1) `sudo apt install nfs-kernel-server`
- (en node1) `mkdir cloud` (en el home)
- (en node1) `sudo nano /etc/exports` afegir 
- `/home/pi/cloud *(rw,sync,no_root_squash,no_subtree_check)`
- (en node1) `sudo chmod -R 777 /home/pi/cloud`
- (en node1) `sudo update-rc.d rpcbind enable`
- (en node1) `sudo service rpcbind restart`
- (en node1) `sudo exportfs -a`
- (en node1) `sudo service nfs-kernel-server restart`


(repetir en tots els nodes)

- (en altreNode) `sudo mkdir ~/cloud`
- (en altreNode) `sudo mount -t nfs node1:/home/pi/cloud ~/cloud`
- (en altreNode) provar que està muntat `df -h`
- (en altreNode) per a fer-ho permanent, editar `/etc/fstab` i afegir la linia: 
  `node1:/home/pi/cloud /home/pi/cloud nfs rw 0 0`
- reset en tots els altresNodes per comprovar que automonta

# Provant el cluster

- Comprovar que tots els nodos estan actius (això hi ha un script per ahi que  ho fa)
- `mpiexec -f machinefile -n 4 hostname` i cada nodo mostrarà el seu nom

nano hello.py

escriure el codi del hello world
escriure un machinfile amb 4 cores per node (4x4 16)

`mpiexec -f machinefile -n 16 python ./hello.py`

# Executar i raonar el funcionament paral·lel del programa

# Images

pip install scipy

Enllaços
- https://mpi4py.readthedocs.io/en/stable/install.html
- https://en.wikipedia.org/wiki/Leibniz_formula_for_π
- https://gist.github.com/jcchurch/930276
- https://www.meccanismocomplesso.org/en/clusters-and-parallel-programming-with-mpi-and-raspberry-pi/
- https://claudiovz.github.io/scipy-lecture-notes-ES/advanced/image_processing/index.html#abriendo-y-escribiendo-archivos-de-imagenes
- https://github.com/arundasan91/MPI---Message-Passing-Interface/blob/master/Image-Scatter-Gather-Tutorial.md
- https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi
- https://nyu-cds.github.io/python-mpi/05-collectives/