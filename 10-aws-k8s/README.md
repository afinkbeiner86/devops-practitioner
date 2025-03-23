# Module 10 - Kubernetes on AWS: EKS


### Project Description
Provision and configure a kubernetes clusters on AWS using following resources and tools:
- IAM: Service Roles, Custom Roles
- ECS/EKS: Nodegroups, Autoscaler, Fargate Profile
- Cloudformation Templates
- ECR
- eksctl

  
Leverage practices and technologies learned from the lectures before  
and use them with ecs and eks services to further enhance our CI/CD pipeline.

#### 1. Create AWS EKS cluster with a Node Group
**Technologies Used:**  
Kubernetes, AWS EKS
  
**Overview**:
- Configure necessary IAM Roles
- Create VPC with Cloudformation Template for Worker Nodes
- Create EKS cluster (Control Plane Nodes)
- Create Node Group for Worker Nodes and attach to EKS cluster
- Configure Auto-Scaling of worker nodes
- Deploy a sample application to EKS cluster

#### 2. Create EKS cluster with Fargate profile
**Technologies Used:**  
Kubernetes, AWS EKS, AWS Fargate
  
**Overview**:
- Create Fargate IAM Role
- Create Fargate Profile
- Deploy an example application to EKS cluster using Fargate profile



#### 3. Create EKS cluster with eksctl
**Technologies Used:**  
Kubernetes, AWS EKS, Eksctl, Linux
  
**Overview**:
- Create EKS cluster using eksctl tool that reduces the manual effort of creating an EKS cluster

#### 4. CD - Deploy to EKS cluster from Jenkins Pipeline
**Technologies Used:**  
Kubernetes, Jenkins, AWS EKS, Docker, Linux
  
**Overview**:
- Install kubectl and aws-iam-authenticator on Jenkins server
- Create kubeconfig file to connect to EKS cluster and add it on Jenkins server
- Add AWS credentials on Jenkins for AWS account authentication
- Extend and adjust Jenkinsfile of the previous CI/CD pipeline to configure connection to EKS cluster

#### 5. CD - Deploy to LKE cluster from Jenkins Pipeline
**Technologies Used:**  
Kubernetes, Jenkins, Linode LKE, Docker, Linux
  
**Overview**:
- Create K8s cluster on LKE
- Install kubectl as Jenkins Plugin
- Adjust Jenkinsfile to use Plugin and deploy to LKE cluster

#### 6. Complete CI/CD Pipeline with EKS and private DockerHub registry
**Technologies Used:**  
Kubernetes, Jenkins, AWS EKS, Docker Hub, Java, Maven, Linux, Docker,Git
  
**Overview**:
- Write K8s manifest files for Deployment and Service configuration
- Integrate deploy step in the CI/CD pipeline:
  - Deploy newly built application image from DockerHub private registry to the EKS cluster

**Current complete CI/CD project configuration:**
- CI steps:
  - Increment version
  - Build artifact for Java Maven application
  - Build and push Docker image to DockerHub
- CD steps:
  - Deploy new application version to EKS cluster
  - Commit the version update

#### 7. Complete CI/CD Pipeline with EKS and AWS ECR
**Technologies Used:**  
Kubernetes, Jenkins, AWS EKS, AWS ECR, Java, Maven, Linux, Docker, Git

Branch for this project: [devops-aws/java-maven-app](https://gitlab.com/devops-training3784615/devops-aws/-/tree/java-maven-app)

**Overview**:
- Create private AWS ECR Docker repository
- Adjust Jenkinsfile to build and push Docker Image to AWS EC
- Integrate deployment to K8s cluster from AWS ECR private registry to CI/CD pipeline

**Current complete CI/CD project configuration:**
- CI steps:
  - Increment version
  - Build artifact for Java Maven application
  - Build and push Docker image to AWS ECR
- CD steps:
  - Deploy new application version to EKS cluster
  - Commit the version update
