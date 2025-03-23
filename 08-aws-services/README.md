# Module 7 - AWS Services

### Project Description
Setup an environment to deploy applications from before projects in AWS  
using ressources and compoments such as:
- IAM: Users, groups, access keys and permissions
- VPCs, subnets, security groups and firewall rules
- EC2 instances
- AWS CLI
  
Leverage practices and technologies learned from the lectures before  
and use them with aws services.

#### 1. Setup EC2 instance and deploy web application manually
**Technologies Used:**  
AWS, Docker, DockerHub, Linux  
  
**Overview**:
- Create and configure an EC2 instance on AWS using the web console
- Install Docker on EC2 instance
- Deploy Docker image from private Docker repository on EC2 instance

#### 2. CD - Deploy application to EC2 instance automatically using Jenkins
**Technologies Used:**  
AWS, Jenkins, Docker, DockerHub, Java, Maven, Git, DigitalOcean, Linux  
  
**Overview**:  
- Prepare AWS EC2 instance for deployment (install Docker)
- Create SSH key pair for EC2 instance and save it as credentials on Jenkins 
- Add deploy step to previous Jenkins CI pipeline to deploy the newly built Docker image to EC2 instance
- Configure firewall rule in security group on EC2 instance to allow access to the web application

#### 3. CD - Deploy application with Jenkins Pipeline & Docker Compose on EC2 instance automatically

**Technologies Used:**  
AWS, Jenkins, Docker, DockerHub, Docker Compose, Java, Maven, Git, DigitalOcean, Linux  
  
**Overview**:  
- Install Docker Compose on AWS EC2 instance
- Create Docker Compose file that deploys our web application image
- Enhance Jenkins pipeline to deploy newly built image using Docker Compose on EC2 server
- Move Linux commands for host preperation and deployment into a shell script. Implement script into pipeline.

#### 4. Complete the CI/CD Pipeline: Docker Compose, dynamic versioning
**Technologies Used:**  
AWS, Jenkins, Docker, DockerHub, Docker Compose, Java, Maven, Git, DigitalOcean, Linux    

**Overview**:  
Pipeline overview:
- CI:
  - Increment version, set Docker image tag
  - Test built and build artifact for Java Maven application
  - Tag, build and push Docker image to Docker Hub
- CD:
  - Deploy new application version with Docker Compose
  - Commit the version update to Git repo

#### 5. Interacting with AWS CLI
**Technologies Used:**  
AWS, Linux  

**Overview**:  
- Install and configure AWS CLI tool to connect to AWS account
- Create EC2 instance using AWS CLI with all necessary configurations such as security groups and subnet
- Create SSH key pair
- Create IAM resources: User, group & policy using AWS CLI
- List and browse AWS resources using AWS CLI and filters


#### Exercise
**Technologies Used:**  
AWS, Jenkins, Docker, Docker Compose, Java, Node.js, Git, DigitalOcean, Linux  
  
**Overview**:  
Prepare AWS resources for hosting a Node.js application.  
Setup CI/CD pipeline for deployment on AWS resources.  

- IAM: Groups, Users, Permissions
  - Created IAM group "devops" with IAM user "bob"
  - Enable the user to create and manage resources like VPC, EC2, security groups, subnets
  - Create credentials for AWS CLI usage
- AWS CLI
  - Set credentials for user created user above
  - Configure region "eu-central-1"
- Create following resources with AWS CLI:
  - VPC, subnet, internet gateway, routing tables
  - Security group with firewall rules 
  - EC2 instance with key pair
- Connect to EC2 instance via SSH and setup docker
- CI/CD:
  - Add docker-compose for deployment
  - Add "deploy to EC2" step to your pipeline
  - Configure access from browser (EC2 Security Group)
  - Configure automatic triggering of pipeline


### Side Notes
**AWS CLI**
Correct syntax for querying policies is:
```
aws iam list-policies --query 'Policies[?PolicyName==`AmazonEC2FullAccess`].Arn' --output text
```
