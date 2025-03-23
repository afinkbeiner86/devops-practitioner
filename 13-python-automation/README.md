# Module 14 - Automation with Python

### Project Description
Provision, control and maintain cloud infrastructure with Python.

#### 1. Health Check: EC2 Status Checks
**Technologies Used:**  
Python, Boto3, AWS, TerraForm
  
**Overview**:  
- Create EC2 instances with TerraForm
- Write a Python script that fetches statuses of EC2 istances and prints to the console
- Extend the Python script to continuously check the status of EC2 Instances in a specific interval

#### 2. Automate configuring EC2 Server Instances
**Technologies Used:**  
Python, Boto3, AWS
  
**Overview**:  
- Write a Python script that automates adding environment tags to all EC2 server instances

#### 3. Automate displaying EKS cluster information
**Technologies Used:**  
Python, Boto3, AWS EKS
  
**Overview**:  
- Write a Python script that fetches and displays EKS cluster status and information


#### 4. Data Backup & Restore
**Technologies Used:**  
Python, Boto3, AWS
  
**Overview**:  
- Write a Python script that automates creating backups for EC2 volumes
- Write a Python script that cleans up old EC2 volume snapshots
- Write a Python script that restores EC2 volumes

#### 5. Website Monitoring and Recovery
**Technologies Used:**  
Python, Linode, Docker, Linux

**Source code for project:** [/src/monitor-website.py](https://gitlab.com/devops-training3784615/python-automation/-/blob/main/src/monitor-website.py)

**Overview**:  
- Create a server on Linode
- Install Docker and run a Docker container on the remote server
- Write a Python script that:
  - Monitors the website by accessing it and validating the HTTP response
  - Sends an email notification when website is down
  - Automatically restarts the application & server when the application is down

---

| Source code of projects above:  [/src](./src)
