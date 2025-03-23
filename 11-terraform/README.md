# Module 11 - Infrastructure as Code with Terraform


### Project Description
Provision, control and document infrastructure as code with TerraForm.

#### 1. Automate AWS Infrastructure
**Technologies Used:**  
Terraform, AWS, Docker, Linux, Git
  
**Overview**:  
Create TF project to automate provisioning AWS Infrastructure and its components.
- Define provider, resources, variables and outputs to provision:
  - VPC, Subnet, Route Table, Internet Gateway, EC2, Security Groups
- Configure TF script to automate deploying Docker container to EC2 instance


#### 2. Modularize Project
**Technologies Used:**  
Terraform, AWS, Docker, Linux, Git
  
**Overview**:  
Move Terraform resources into reusable modules using best practices and standards:
- Prepare folder and file structure for modules
- Move resources from main.tf to module
- Move variables from main.tf to module
- Implement modules in main.tf

#### 3. Provision AWS EKS
**Technologies Used:**  
Terraform, AWS EKS, Docker, Linux, Git
  
**Overview**:  
Automate EKS cluster provisioning with Terraform:
 - Provision VPC using the TF module "AWS VPC"
 - Provision EKS using the TF module "AWS EKS"
 - Declare variables and implement the references

#### 4. TerraForm Remote State
**Technologies Used:**  
Terraform, AWS S3
  
**Overview**:  
- Configure Amazon S3 bucket as remote storage for TerraForm state
- Create Makefile to quickly create/destroy s3 bucket

#### 5. Complete CI/CD with Terraform
**Technologies Used:**  
Terraform, Jenkins, Docker, AWS, Git, Java, Maven, Linux, Docker Hub
  
**Overview:**  
Integrate provisioning stage into CI/CD pipeline to automate provisioning infrastructure. 
 
Branch for this project: [feature/jenkins-ci-cd](https://gitlab.com/devops-training3784615/devops-terraform/-/tree/feature/jenkins-ci-cd)

- Create RSA key pair
- Install TerraForm inside Jenkins container
- Add Terraform configuration to application git repository
- Implement 'provision' step to Jenkinsfile
  
**Current complete CI/CD project configuration:**
  
CI steps:  
- Build artifact for Java Maven application 
- Build and push Docker image to Docker hub
  
CD steps:
- Provision EC2 instance using TerraForm
- Deploy new application version on the provisioned EC2 instance with Docker Compose
