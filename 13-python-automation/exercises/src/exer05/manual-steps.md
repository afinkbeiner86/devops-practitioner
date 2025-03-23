```sh
# Install Python inside Jenkins server
apt-get install python3
apt-get install pip
pip install boto3
pip install paramiko
pip install requests

# Create credentials in Jenkins
"jenkins_aws_access_key_id" - Secret Text
"jenkins_aws_secret_access_key" - Secret Text
"ssh-creds" - SSH Username with private key
"ecr-repo-pwd" - Secret Text
```
```sh
# Set following ENV_VARS before executing the pipeline
- ECR_REPO_NAME
- EC2_SERVER
- ECR_REGISTRY
- CONTAINER_PORT
- HOST_PORT
- AWS_DEFAULT_REGION
```
