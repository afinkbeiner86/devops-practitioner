#### Exercise 1: Build & Deploy Java Artifact
You want to help developers automate deploying a Java application on a remote server directly from their local environment. So you create an Ansible project that builds the java application in the Java-gradle project. Then deploys the built jar artifact to a remote Ubuntu server.

Developers will execute the Ansible script by specifying their first name as the Linux user which will start the application on a remote server. If the Linux User for that name doesn't exist yet on the remote server, Ansible playbook will create it.

Also consider that the application may already be running from the previous jar file deployment, so make sure to stop the application and remove the old jar file from the remote server first, before copying and deploying the new one, also using Ansible.

#### Exercise 2: Push Java Artifact to Nexus
Developers like the convenience of running the application directly from their local dev environment. But after they test the application and see that everything works, they want to push the successful artifact to Nexus repository. So you write a play book that allows them to specify the jar file and pushes it to the team's Nexus repository.

#### Exercise 3: Install Jenkins on EC2
Your team wants to automate creating Jenkins instances dynamically when needed. So your task is to write an Ansible code that creates a new EC2 server and installs and runs Jenkins on it. It also installs nodejs, npm and docker to be available for Jenkins builds.

Now your team can use this project to spin up a new Jenkins server with 1 Ansible command.

#### Exercise 4: Install Jenkins on Ubuntu
Your company has infrastructure on multiple platforms. So in addition to creating the Jenkins instance dynamically on an EC2 server, you want to support creating it on an Ubuntu server too. Your task it to re-write your playbook (using include_tasks or conditionals) to support both flavors of the OS.

#### Exercise 5: Install Jenkins as a Docker Container
In addition to having different OS flavors as an option, your team also wants to be able to run Jenkins as a docker container. So you write another playbook that starts Jenkins as a Docker container with volumes for Jenkins home and Docker itself, because you want to be able to execute Docker commands inside Jenkins.

Here is a reference of a full docker command for starting Jenkins container, which you should map to Ansible playbook:

```bash
docker run --name jenkins -p 8080:8080 -p 50000:50000 -d \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /usr/local/bin/docker:/usr/bin/docker \
-v jenkins_home:/var/jenkins_home \
jenkins/jenkins:lts
```

Your team is happy, because they can now use Ansible to quickly spin up a Jenkins server for different needs.

Use repository: https://gitlab.com/devops-bootcamp3/bootcamp-java-mysql

#### Exercise 6: Web server and Database server configuration
Great, you have helped automate some IT processes in your company. Now another team wants your support as well. They want to automate deploying and configuring web server and database server on AWS. The project is not dockerized and they are using a traditional application setup.

The setup you and the team agreed on is the following: You create a dedicated Ansible server on AWS. In the same VPC as the Ansible server, you create 2 servers, 1 for deploying your Java application and another one for running a MySQL database. Also, the database should not be accessible from outside, only within the VPC, so the DB server shouldn't have a public IP address.

So your task is to:

Provision and configure dedicated Ansible server

- Write Ansible playbook that provisions a dedicated ansible-control plane server
- Write Ansible playbook that configures the ansible server with all needed tools as well as copies all needed ansible
  playbooks and configuration for execution there
  
Provision and configure databse and web servers:

- Write Ansible playbook that provisions database and web servers.
- Write Ansible playbook that installs and starts MySQL server on the EC2 instance without public IP address,  
  deploys and runs the Java web application on another EC2 instance

NOTES:

- Use an existing mysql role for installing mysql on the database server, instead of writing the whole logic yourself
- The last 2 playbooks for provisioning and configuring web and database servers will be executed from Ansible control server, because we can't access the database private IP address from outside VPC
- Since the database server will have no public IP address, it will not have a direct internet access. But we will need to download and install some tools, like mysql service itself on the server, and you can do it via NAT gateway. So make sure to create database server in a "private" subnet, with NAT gateway instead of Internet gateway configuration.
Once all the playbooks executed successfully, check that the java application is running and accessible from browser at http://web-server-public-address:8080


#### Exercise 7: Deploy Java MySQL Application in Kubernetes
After some time, the team decides they want to move to a more modern infrastructure setup, so they want to dockerize their application and start deploying to a K8s cluster.

However, K8s is a very new tool for them, and they don't want to learn kubectl and K8s configuration syntax and how all that works, so they want the deployment process to be automated so that it's much easier for them to deploy the application to the cluster without much K8s knowledge.

So they ask you to help them in the process. You create K8s configuration files for deployments, services for Java and MySQL applications as well as configMap and Secret for the Database connectivity. You also want to access your web application from browser, so you will have to deploy nginx-ingress controller chart and create ingress component for your java app. And you deploy everything in a cluster using an Ansible automated script.

Note: MySQL application will run as 1 replica and for the Java Application you will need to create and push an image to a Docker repo. You can create the K8s cluster with TF script or any other way you prefer.

#### Exercise 8: Deploy MySQL Chart in Kubernetes
Everything works great, but the team worries about the application availability, so wants to run the MySQL DB in multiple replicas. So they ask you to help them solve this problem. Your task is to deploy a MySQL with 3 replicas from a helm chart using Ansible script in place of the currently running single MySQL instance.
