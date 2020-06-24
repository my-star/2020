#  Ansible install and config
> The test environment is centos in docker
#### Docker run command
```bash
    sudo docker run --name ansible -d centos /bin/bash
   
    sudo docker ps -a
    
    sudo docker attach ansible

    root@ansible # sudo yum -y install epel-release

    root@ansible # sudo yum -y install ansible
```
##### display ansible version
```bash
    $ ansible --version
```
I get a problem in the docker

> System has not been booted with systemd as init system(PID 1),Can't operate.
Failed to connect to bus: Host is down
