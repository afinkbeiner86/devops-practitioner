## AWS CLI EC2 setup
#### Exercise 1-3
- Create IAM user with EC2 and VPC permissions
- Configure AWS CLI access keys for created users
- Create a new VPC with 1 subnet
- Configure internet gateway and routes for subnet
- Create a security group in the VPC that will allow:
  - Admin ssh access on port 22
  - Browser access to your Node application

```bash
# Create vpc
aws ec2 create-vpc \
    --cidr-block 10.0.0.0/28 \
    --tag-specification 'ResourceType=vpc,Tags=[{Key=Name,Value=DevopsVpc}]'

# Enable DNS hostnames for the vpc
aws ec2 modify-vpc-attribute --vpc-id vpc-0497eb0a1138cc53a --enable-dns-hostnames "{\"Value\":true}"

# Create subnet
aws ec2 create-subnet \
    --vpc-id vpc-0497eb0a1138cc53a \
    --cidr-block 10.0.0.0/28 \
    --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=devops-subnet}]'

# Enable public IP mapping
aws ec2 modify-subnet-attribute --subnet-id subnet-0769ea9b7c9af527e --map-public-ip-on-launch

# Create internet gateway and query id
aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text

# Attach internet gateway to vpc
aws ec2 attach-internet-gateway --vpc-id vpc-0497eb0a1138cc53a --internet-gateway-id igw-09fff31e9a86c4479

# Create route table and query id
aws ec2 create-route-table --vpc-id vpc-0497eb0a1138cc53a --query RouteTable.RouteTableId --output text

# Create Route rule for handling all traffic between internet & VPC
aws ec2 create-route --route-table-id rtb-036d8f5543897f8e9 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-09fff31e9a86c4479

# Valide route table configuraton: 1 local and 1 interent gateway routes
aws ec2 describe-route-tables --route-table-id rtb-036d8f5543897f8e9

# Associate subnet with the route table to allow internet traffic in the subnet as well
aws ec2 associate-route-table  --subnet-id subnet-0769ea9b7c9af527e --route-table-id rtb-036d8f5543897f8e9

```

```bash
# Create security group and rules for ssh admin acces
aws ec2 create-security-group --group-name DevopsSG --description "DevOps security group" --vpc-id vpc-0497eb0a1138cc53a
aws ec2 authorize-security-group-ingress --group-id sg-0908608d0d5ce0afd --protocol tcp --port 22 --cidr 178.2.184.90/32
```

#### Exercise 4
Create EC2 instance with key pair and attach it to security group
```bash
# Create key pair and set file permissions
aws ec2 create-key-pair --key-name webserver-key --key-format pem --query KeyMaterial --output text >> webserver.pem \
&& chmod 400 webserver.pem

#Create EC2 instance with all resources we created in the steps before
aws ec2 run-instances --image-id ami-06c39ed6b42908a36 \
--count 1 \
--instance-type t2.micro \
--key-name webserver-key \
--security-group-ids sg-0908608d0d5ce0afd \
--subnet-id subnet-0769ea9b7c9af527e

# Validate that EC2 instance is in a running state, and get its public ip address to connect via ssh
aws ec2 describe-instances --instance-id i-07ff957d7e89969fd --query "Reservations[*].Instances[*].{State:State.Name,Address:PublicIpAddress}"

```

#### Exercise 5
Connect to EC2 instance and install docker
```bash
# Connect via ssh and rsa key
ssh -i webserver.pem ec2-user@public-ec2-ip

# Update system packages, install docker, add ec2-user to docker group
sudo yum update -y
sudo yum install docker -y
sudo usermod -aG docker ec2-user

# Enable docker daemon, start docker and verfiy if it's running
systemctl enable docker && systemctl start docker
docker ps
```
## CI/CD with Jenkins to EC2 Instance
Solution to the following steps are in this branch: https://gitlab.com/devops-training3784615/devops-aws/-/tree/nodejs-app
  
- Exercise 6: Add docker-compose for deployment 
- Exercise 7: Add "deploy to EC2" step to your pipeline
- Exercise 9: Configure automatic triggering of pipeline

#### Exercise 8
Configure access from browser (EC2 Security Group)
```bash
aws ec2 authorize-security-group-ingress --group-id sg-0908608d0d5ce0afd --protocol tcp --port 3000 --cidr 0.0.0.0/0
```
