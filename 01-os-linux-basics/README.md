# Module 1 - Operating Systems & Linux Basics

#### Exercise 1: Linux Mint VM
Download and follow official guide:
- https://linuxmint.com/download.php
- https://linuxmint-installation-guide.readthedocs.io/en/latest/

#### Exercise 2-9: Bash Scripting
- Install Java
- List sorted user proccesses
- Start Node.js app
- Start Node.js app with service user & log directory
  
| [Solutions Bash Scripting](https://gitlab.com/devops-training3784615/os-linux-basics/-/tree/main/bash-scripting)

#### Environment, Testing & Deployment
Didn't want to mess up my RPI so I decided to use a Docker container running Ubuntu to test and run the scripts and programs from the exercises.  
```bash
#Spin up Ubuntu container with volume mount to host file system:
docker run --detach-keys='ctrl-z,z' -it -v "$(pwd)":/srv ubuntu:focal
```
