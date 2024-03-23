import docker

def getContainerIds():
    client = docker.from_env()
    containers = client.containers.list()
    container_ids = [container.id[:12] for container in containers]
    return container_ids

def getContainerNames():
    client = docker.from_env()
    containers = client.containers.list()
    container_names = [container.name for container in containers]
    return container_names

def reset_etc_hosts(containers):
    client = docker.from_env()

    for c in containers:
        container = client.containers.get(c)
        exec_result = container.exec_run(['head', '-n', '7', '/etc/hosts'])  # Modify this line
        seven_lines = exec_result.output.decode().strip()
        exec_result = container.exec_run(['bash', '-c', f"echo '{seven_lines}' > /etc/hosts"])
        if exec_result.exit_code != 0:
            print(f"Failed to add lines to /etc/hosts in container {c}")    

def get_last_line_from_hosts_file(containers):
    client = docker.from_env()
    last_lines = []

    for c in containers:
        container = client.containers.get(c)
        exec_result = container.exec_run(['tail', '-n', '1', '/etc/hosts'])
        last_line = exec_result.output.decode().strip()
        last_lines.append(last_line)

    return last_lines

def add_lines_to_hosts_file(containers, lines):
    client = docker.from_env()
    for c in containers:
        container = client.containers.get(c)
        exec_result = container.exec_run(['bash', '-c', f"echo '{lines}' >> /etc/hosts"])
        if exec_result.exit_code != 0:
            print(f"Failed to add lines to /etc/hosts in container {c}")

def add_lines_to_machinefile(containers, lines):
    client = docker.from_env()
    for c in containers:
        container = client.containers.get(c)
        exec_result = container.exec_run(['bash', '-c', f"echo '{lines}' > /etc/machinefile"])
        if exec_result.exit_code != 0:
            print(f"Failed to add lines to /etc/machinefile in container {c}")

def add_names_to_machinefile(containers, names):
    client = docker.from_env()
    for c in containers:
        container = client.containers.get(c)
        exec_result = container.exec_run(['bash', '-c', f"echo '{names}' > /etc/machinefile"])
        if exec_result.exit_code != 0:
            print(f"Failed to add lines to /etc/machinefile in container {c}")

def versio_amb_noms():
    names=getContainerNames()
    running_containers=getContainerIds()
    print(running_containers)
    print(names)
    (host,IP)=get_IP_head(running_containers)
    print(f"Host principal és: {host}, IP: {IP}")
    print(f"La connexio serà ssh -i docker.openmpi/ssh/id_rsa.mpi  mpirun@{IP}")
    print("Afegint la resta de hosts al machinefile")
    add_names_to_machinefile(running_containers, "\n".join(names))

def versio_amb_ips():
    running_containers=getContainerIds()
    print(running_containers)

    reset_etc_hosts(running_containers)

    hosts=get_last_line_from_hosts_file(running_containers)
    print(hosts)

    lines = "\n".join(hosts)
    print(lines)

    machines="\n".join([h.split("\t")[1]+":2" for h in hosts])
    print(machines)

    add_lines_to_hosts_file(running_containers, lines)
    add_lines_to_machinefile(running_containers, machines)

def get_IP_head(containers):
    client = docker.from_env()
    for c in containers:
        container = client.containers.get(c)
        name=container.name
        if 'head' in name:
            exec_result = container.exec_run(['tail', '-n', '1', '/etc/hosts'])
            line = exec_result.output.decode().strip()   
            IP=line.split("\t")[0]
            host=line.split("\t")[1]
            break

    return host,IP 


def main():
   versio_amb_noms()  
   
if __name__ == "__main__":  
    main()