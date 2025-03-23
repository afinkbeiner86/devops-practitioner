#### Exercise 1: Create Terraform project to spin up EKS cluster
Create a Terraform project that spins up an EKS cluster with the exact same setup that you created in the previous exercise, for the same Java Gradle application:
  
- Create EKS cluster with 3 Nodes and 1 Fargate profile only for your java application
- Deploy Mysql with 3 replicas with volumes for data persistence using helm
  
Create a separate git repository for your Terraform project, separate from the Java application, so that changes to the EKS cluster can be made by a separate team independent of the application changes themselves.

#### Exercise 2: Configure remote state
By default, TF stores state locally. You know that this is not practical when working in a team, because each user must make sure they always have the latest state data before running Terraform. To fix that, you configure remote state with a remote data store for your terraform project. You can use e.g. S3 bucket for storage.
  
- Create AWS S3 bucket
- Configure TerraForm to use S3 bucket for remote state

#### Exercise 3: CI/CD pipeline for TerraForm project
- Create a separate Jenkins pipeline for Terraform provisioning the EKS cluster
  
Solutions: [exercise/eks-java-mysql](https://gitlab.com/devops-training3784615/devops-terraform/-/tree/exercise/eks-java-mysql/)
