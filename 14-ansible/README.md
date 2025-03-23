# Module 14 - Configuration Management with Ansible

### Project Description
Configure systems, deploy software or orchestrate more advanced IT tasks using Ansible


#### 1. Automate Node.js application Deployment
**Technologies Used:**  
Ansible, Node.js, DigitalOcean, Linux
  
**Overview**:  
- Create Server on DigitalOcean
- Write Ansible Playbook for following tasks:
  - Install dependencies
  - Creates Linux user to run an application
  - Deploy a Node.js application with that user


#### 2. Automate Nexus Deployment
**Technologies Used:**  
Ansible, Nexus, DigitalOcean, Java, Linux
  
**Overview**:  
- Create Server on DigitalOcean
- Write Ansible Playbook for following tasks:
  - Create Linux user for Nexus
  - Configure server
  - Install Nexus
  - Verify that Nexus is running

#### 3. Ansible & Docker
**Technologies Used:**  
Ansible, AWS, Docker, Terraform, Linux
  
**Overview**:  
- Create AWS EC2 Instance with Terraform
- Write Ansible Playbook for following tasks:
  - Install dependencies (Docker, docker-compose etc.)
  - Copy docker-compose file to server
  - Run docker-compose


#### 4. Ansible Integration in Terraform
**Technologies Used:**  
Ansible, Terraform, AWS, Docker, Linux
  
**Overview**:  
- Create Ansible Playbook for Terraform integration
- Adjust Terraform configuration:
  - Provision server
  - Run Ansible Playbook to configure server


#### 5. Configure Dynamic Inventory
**Technologies Used:**  
Ansible, Terraform, AWS
  
**Overview:**  
- Create EC2 Instance with Terraform
- Write Ansible AWS EC2 Plugin to dynamically set inventory of EC2 servers  
  that Ansible should manage instead of hard-coding server addresses in Ansible inventory file
  
#### 6. Automate Kubernetes Deployment
**Technologies Used:**  
Ansible, Terraform, Kubernetes, AWS EKS, Python, Linux
  
**Overview**:  
- Create EKS cluster with Terraform: [terraform/eks](https://gitlab.com/devops-training3784615/devops-terraform/-/tree/feature/eks/terraform)
- Write Ansible Play to deploy application in a new K8s namespace: [deploy-to-k8s.yaml](https://gitlab.com/devops-training3784615/14-ansible/-/blob/main/deploy-to-k8s.yaml)


#### 7. Ansible Integration in Jenkins
**Technologies Used:**  
Ansible, Jenkins, DigitalOcean, AWS, Boto3, Docker, Java, Maven, Linux, Git  

Link to branch for this project: [feature/jenkins](https://gitlab.com/devops-training3784615/14-ansible/-/tree/feature/jenkins)

**Overview:**  
- Create and configure a dedicated server for Jenkins
- Create and configure a dedicated server for Ansible Control Node
- Write Ansible Playbook to configure 2 EC2 Instances
- Add ssh key file credentials in Jenkins for Ansible Control Node server and Ansible Managed Node servers
- Configure Jenkins to execute the Ansible Playbook on remote Ansible Control Node server as part of the CI/CD pipeline
- Jenkinsfile Pipeline tasks:
  - Connect to the remote Ansible Control Node server
  - Copy Ansible Playbook and configuration files to the remote Ansible Control Node server
  - Copy the ssh keys for the Ansible Managed Node servers to the Ansible Control Node server
  - Install Ansible, Python3 and Boto3 on the Ansible Control Node server
  - Execute Ansible Playbook remotely on Control Node to configure the 2 EC2 Managed Nodes


#### 8. Structure Playbooks with Ansible Roles
**Technologies Used:**  
Ansible, Docker, AWS, Linux
  
**Overview**:  
- Break up large Ansible Playbooks into smaller and more manageable files using Ansible Roles
