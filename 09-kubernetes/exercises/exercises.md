## 10 - Container Orchestration with Kubernetes

#### Exercise 1
Create a Kubernetes cluster (Minikube or LKE)
- Created K8s cluster using LKE on Linode WebUI

#### Exercise 2
Deploy Mysql database with 3 replicas and volumes for data persistence
- Created values file for mysql helm chart deployment
- Deployed via helm to LKE 

#### Exercise 3
Deploy your Java Application with 3 replicas
- Create deployment, configmap and secrets file
- In the deployment file, refer to key/values from configmaps and secrets
- Apply all files to cluster

#### Exercise 4
Deploy phpmyadmin
- Create deployment file and refer to key/values from configmap.
- Apply deployment to cluster

#### Exercise 5
Deploy Ingress Controller
- Install ingress controller using helm:
```bash
helm install nginx-ingress bitnami/nginx-ingress-controller --set controller.publishService.enabled=true
```

#### Exercise 6
Create Ingress rule
- Create ingress rule file using nginx ingress controller
- Refer to java-mysql-service and LKE load balancer node

#### Exercise 7 
Configure port-forward for phpmyadmin
```bash
kubectl port-forward svc/phpmyadmin-service 8081:8081
```

#### Exercise 8
Create Helm charts for Java App
- Create template files for each resource:
  - Deployment, Service, Ingress
  - CofifMap, Secret
- Create default values file
- Create values file with real values
- Test deployment
