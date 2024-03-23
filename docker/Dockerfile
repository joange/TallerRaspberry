# Ens basem ambuna ubuntu 18
FROM ubuntu:18.04

# ------------------------------------------------------------
# Alguines variables d'entorn
# ------------------------------------------------------------

# L'usuari dels nodes
ENV USER mpirun

# Diguem que la instalació siga desatesa (no interactiva)
ENV DEBIAN_FRONTEND=noninteractive 

#Creem el home de l'usuari
ENV HOME=/home/${USER} 

# Instal·lem tot el necessari
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends sudo apt-utils && \
    apt-get install -y --no-install-recommends openssh-server \
        python-dev python-numpy python-pip python-virtualenv python-scipy \
        gcc gfortran libopenmpi-dev openmpi-bin openmpi-common openmpi-doc binutils && \
    apt-get install -y --no-install-recommends nano && \
    apt-get install -y --no-install-recommends git && \
    apt-get install -y --no-install-recommends inetutils-ping && \
    apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ------------------------------------------------------------
# Crea un directori anomenat sshd a la ruta /var/run/. 
# Aquest directori s'utilitza per emmagatzemar informació en temps 
# d'execució per al servidor SSH
# ------------------------------------------------------------
RUN mkdir /var/run/sshd

# ------------------------------------------------------------
# Establim el password de root com l'usuari 
# ------------------------------------------------------------
RUN echo 'root:${USER}' | chpasswd

# ------------------------------------------------------------
# Aquesta comanda modifica el fitxer de configuració del servidor SSH, sshd_config. 
# Permetent l'inici de sessió com a root sense contrasenya. 
# Canvia PermitRootLogin without-password per PermitRootLogin yes
# ------------------------------------------------------------
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config


# ------------------------------------------------------------
# Fixa el login SSH login fix. Per no expulsar l'usuari desprès del login
# ------------------------------------------------------------
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# ------------------------------------------------------------
# Configuracions adicionals
# ------------------------------------------------------------
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# ------------------------------------------------------------
# Afegim l'usuari  'mpirun'
#       sense password
#       amb privilegis de sudo
# ------------------------------------------------------------

RUN adduser --disabled-password --gecos "" ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# ------------------------------------------------------------
# Set-Up SSH with our Github deploy key (original)
# ------------------------------------------------------------


# ------------------------------------------------------------
# Creem el directori del ssh server
# ------------------------------------------------------------

ENV SSHDIR ${HOME}/.ssh/
RUN mkdir -p ${SSHDIR}

# ------------------------------------------------------------
# Copiem les claus públiques i privades originals
# Ademés afegim la publica com a authorized keys
# Per poder fer login automàtic
# ------------------------------------------------------------
ADD ssh/config ${SSHDIR}/config
ADD ssh/id_rsa.mpi ${SSHDIR}/id_rsa
ADD ssh/id_rsa.mpi.pub ${SSHDIR}/id_rsa.pub
ADD ssh/id_rsa.mpi.pub ${SSHDIR}/authorized_keys

RUN chmod -R 600 ${SSHDIR}* && \
    chown -R ${USER}:${USER} ${SSHDIR}


# ------------------------------------------------------------
# Actualitzem el pip
# ------------------------------------------------------------
RUN pip install --upgrade pip


# ------------------------------------------------------------
# Instal·lem mpi4py
# ------------------------------------------------------------
USER ${USER}
RUN  pip install --user -U setuptools \
    && pip install --user mpi4py

# ------------------------------------------------------------
# Configurem OpenMPI
# ------------------------------------------------------------

USER root

RUN rm -fr ${HOME}/.openmpi && mkdir -p ${HOME}/.openmpi
ADD default-mca-params.conf ${HOME}/.openmpi/mca-params.conf
RUN chown -R ${USER}:${USER} ${HOME}/.openmpi


# ------------------------------------------------------------
# Clonem el repo del taller
# ------------------------------------------------------------
WORKDIR ${HOME}
RUN git clone https://github.com/joange/TallerRaspberry.git



# Exposem el port 22 i arranquem el servidor ssh
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]