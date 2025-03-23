#### Exercise 1: Create EKS cluster and fargate profile using eksctl
```bash
# Create eks cluster with 3 nodes
eksctl create cluster \
--name exercise-cluster \
--version 1.25 \
--region eu-central-1 \
--nodegroup-name exercise-nodes \
--node-type t2.micro \
--nodes 3 \
--nodes-min 1 \
--nodes-max 3 \
--kubeconfig=./kubeconfig.my-cluster.yaml

# Create fargate profile
eksctl create fargateprofile \
    --cluster exercise-cluster \
    --name exercise-fargate-profile \
    --namespace my-app \

# Validate cluster is accessible and nodes and fargate profile created
kubectl get node
eksctl get fargateprofile --cluster my-cluster
```
#### Exercise 2: Deploy mysql and phpmyadmin on EKS cluster
```bash
# Using helm charts for mysql as before
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/mysql -f mysql-eks-values.yml

# Deploy configmaps, secrets and phpmyadmin
kubectl apply -f config-maps.yaml
kubectl apply -f secrets.yaml
kubectl apply -f phpmyadmin.yaml

# Enable port forwarding to phpmyadmin service
kubectl port-forward svc/phpmyadmin-service 8081:8081

# Login on local browser to verify if all is working
localhost:8081
```

#### Exercise 3: Deploy Java Application on EKS cluster with 3 replicas
```bash
# Create namespace my-app to deploy our java application into.
# The fargate profile we created before refers to namespace 'my-app'.
kubectl create namespace my-app

# If your docker repo is private, you'd have to create a secret like so:

# Create my-registry-key secret to pull image 
DOCKER_REGISTRY_SERVER=docker.io
DOCKER_USER=your dockerID, same as for `docker login`
DOCKER_EMAIL=your dockerhub email, same as for `docker login`
DOCKER_PASSWORD=your dockerhub pwd, same as for `docker login`

kubectl create secret -n my-app docker-registry my-registry-key \
--docker-server=$DOCKER_REGISTRY_SERVER \
--docker-username=$DOCKER_USER \
--docker-password=$DOCKER_PASSWORD \
--docker-email=$DOCKER_EMAIL

# Finally deploy secrets, configmap and java-app deployment to namespace 'my-app'
kubectl apply -f secrets.yaml -n my-app
kubectl apply -f config-maps.yaml -n my-app
kubectl apply -f java-mysql-deployment.yaml -n my-app
```

#### Exercise 4 & 5: Automate deployment & use ECR as Docker repository
```bash
# Create a docker registry secret for ECR
DOCKER_REGISTRY_SERVER=your ECR registry server - "your-aws-id.dkr.ecr.your-ecr-region.amazonaws.com"
DOCKER_USER=your dockerID, same as for `docker login` - "AWS"
DOCKER_PASSWORD=your dockerhub pwd, same as for `docker login` - get using: "aws ecr get-login-password --region {ecr-region}"

kubectl create secret -n my-app docker-registry my-ecr-registry-key \
--docker-server=$DOCKER_REGISTRY_SERVER \
--docker-username=$DOCKER_USER \
--docker-password=$DOCKER_PASSWORD


# Make all tools needed for operating EKS/ECR available to Jenkins:

# Enter Jenkins container
sudo docker exec -it {jenkins-container-id} -u 0 bash

# Install aws-cli
# Link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install

# Install kubectl
# - Link: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

apt-get update
apt-get install -y apt-transport-https ca-certificates curl
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl

# Install envsubst tool
# - Link: https://command-not-found.com/envsubst

apt-get update
apt-get install -y gettext-base

# Create 2 "secret-text" credentials for AWS access in Jenkins: 
- "jenkins_aws_access_key_id" for AWS_ACCESS_KEY_ID 
- "jenkins_aws_secret_access_key" for AWS_SECRET_ACCESS_KEY    

# Create 4 "secret-text" credentials for db-secret.yaml:
- id: "db_user", secret: "my-user"
- id: "db_pass", secret: "my-pass"
- id: "db_name", secret: "my-app-db"
- id: "db_root_pass", secret: "secret-root-pass"

# Set the correct values in Jenkins for following environment variables: 
- ECR_REPO_URL
- CLUSTER_REGION
```
Create Jenkinsfile with all the neccessary steps to complete the pipeline:
[Deploy on EKS Pipeline](https://gitlab.com/devops-training3784615/devops-aws/-/tree/deploy-on-eks)

#### Exercise 6: Configure Autoscaling

Create custom policy as JSON in AWS:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "autoscaling:DescribeLaunchConfigurations",
                "autoscaling:DescribeTags",
                "autoscaling:SetDesiredCapacity",
                "autoscaling:TerminateInstanceInAutoScalingGroup",
                "ec2:DescribeLaunchTemplateVersions"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```
- Attach policy to NodeGroup Role of the EKS cluster

```bash
# Download kubernetes auto-scaler deployment
curl https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml -o cluster-autoscaler-autodiscover.yaml -s

# Configure deployment to match our cluster
cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
node-group-auto-discovery=asg:tag=k8s.io/cluster-autoscaler/enabled,k8s.io/cluster-autoscaler/exercise-cluster
--balance-similar-node-groups
--skip-nodes-with-system-pods=false
image: registry.k8s.io/autoscaling/cluster-autoscaler:v1.25.1

# Deploy the auto-scaler
kubectl apply -f cluster-autoscaler-autodiscover.yaml
```
