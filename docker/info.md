# Introducció 

> Aquest material és una recerca temporal de com crear un laboratori de treball amb mpi fetn servir contenidors docker com a nodes de treball


## Punt de partida

Crear un contenidor amb tot el necessari. Amb el següent dockerfile:

```dockerfile
FROM nlknguyen/alpine-mpich

# Install python/pip
USER root

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
```

On:

- `nlknguyen/alpine-mpich` està basat amb alpine i te mpi
- Amb les altres comandes instalem `python3` i `pip`


# Creació de un cluster amb varies imatges `openmpi`

<https://github.com/oweidner/docker.openmpi>

## Opció que funciona

Llançar 1 master i 1 node

```bash
# No funciona
# docker-compose scale mpi_head=1 mpi_node=2

# Si funciona
docker compose up -d --scale mpi_head=1  --scale mpi_node=1
```

Aturar els contenedors

```bash
docker compose down
```


docker-compose exec --privileged mpi_head mpirun -n 2 python /home/mpirun/mpi4py_benchmarks/all_tests.py


