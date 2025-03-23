# 09 - Container Orchestration with Kubernetes

### Project Description
This modules teaches about container orchestration with kubernetes.
  
Leverage practices and technologies learned from the lectures before  
and combine them with kubernetes.

---

#### 1. Deploy MongoDB and Mongo Express into local K8s cluster
**Technologies Used:**  
Kubernetes, Docker, MongoDB, Mongo Express 
  
**Overview**:
- Setup local K8s cluster with Minikube
- Create deployment files for MongoDB and MongoExpress
- Create corresponding service to MongoDB and MongoExpress deployments
- Create Secret to be used by both deployments
- Create ConfigMap to be used by MongoExpress deployment

#### 2. Deploy Mosquitto message broker with ConfigMap and Secret Volume Types
**Technologies Used:**  
Kubernetes, Docker, Mosquitto

**Overview**:
- Define configuration and passwords for Mosquitto message broker with ConfigMap and Secret Volume types

#### 3. Install a stateful service (MongoDB) on Kubernetes using Helm
**Technologies Used:**  
Kubernetes, Helm, MongoDB, Mongo Express, Linode LKE, Linux

**Overview**:
- Create a managed K8s cluster with Linode Kubernetes Engine
- Deploy replicated MongoDB service in LKE cluster using a Helm chart
- Configure data persistence for MongoDB with Linode’s cloud storage
- Deploy UI client Mongo Express for MongoDB
- Deploy and configure nginx ingress to access the UI application from browser

#### 4. Deploy our web application in K8s cluster from private Docker registry
**Technologies Used:**  
Kubernetes, Helm, AWS ECR, Docker

**Overview**:
- Create Secret for credentials for the private Docker registry
- Configure the Docker registry secret in application Deployment component
- Deploy web application image from our private Docker registry in K8s cluster

#### 5. Setup Prometheus Monitoring in Kubernetes cluster
**Technologies Used:**  
Kubernetes, Helm, Prometheus

**Overview**:
- Deploy Prometheus in local Kubernetes cluster using a Helm chart

#### 6. Deploy Microservices application in Kubernetes with Production & Security Best Practices
**Technologies Used:**
Kubernetes, Redis, Linux, Linode LKE

**Link to files:** [online-shop-microservices](https://gitlab.com/devops-training3784615/devops-kubernetes/-/tree/main/demo-projects/online-shop-microservices)

**Overview**:
- Create K8s manifests for Deployments and Services for all microservices of an online shop application
- Deploy microservices to Linode’s managed Kubernetes cluster

#### 7. Create Helm Chart for Microservices
**Technologies Used:**
Kubernetes, Helm
  
**Overview**:
- Create 1 shared Helm Chart for all microservices, to reuse common Deployment and Service configurations for the services

#### 7. Deploy Microservices with Helmfile
**Technologies Used:**
Kubernetes, Helm, Helmfile
  
**Overview**:
- Deploy Microservices with Helm
- Deploy Microservices with Helmfile

---

### Exercises
See [exercises.md](/exercises/exercises.md)

---

### Side Notes
Setup minikube locally
```bash
# Install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb

# Configure kubectl for minikube (create symlink to minikube command)
sudo ln -s $(which minikube) /usr/local/bin/kubectl
```
Bind localhost:port to minikube external service
```bash
minikube service $serviceName
```
