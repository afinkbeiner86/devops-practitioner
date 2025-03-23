# 15 - Monitoring with Prometheus
### Project Description
Setup Prometheus Monitoring and Alerting for third-party or own applications.


#### 1. Install Prometheus Stack in Kubernetes
**Technologies Used:**  
Prometheus, Kubernetes, Helm, AWS EKS, eksctl, Grafana, Linux
  
**Overview**:  
- Setup EKS cluster using eksctl
- Deploy Prometheus, Alert Manager and Grafana in cluster as
  part of the Prometheus Operator using Helm chart


#### 2. Configure Alerting for our Application
**Technologies Used:**  
Prometheus, Kubernetes, Linux
  
**Overview**:  
- Configure our Monitoring Stack to notify us when:
  - CPU usage > 50%
  - Pod not started
- Configure Alert Rules in Prometheus Server
- Configure Alertmanager with Email Receiver

#### 3. Configure Monitoring for a Third-Party Application
**Technologies Used:**  
Prometheus, Kubernetes, Redis, Helm, Grafana
  
**Overview**:  
Monitor Redis by using Prometheus Exporter
- Deploy Redis service in our cluster
- Deploy Redis exporter using Helm Chart
- Configure Alert Rules: Redis down or too many connections
- Import Grafana Dashboard for Redis to visualize monitoring data in Grafana


#### 4. Configure Monitoring for Own Application
**Technologies Used:**  
Prometheus, Kubernetes, Node.js, Grafana, Docker, Docker Hub

**Overview**:  
- Configure Node.js application to collect and expose Metrics with Prometheus Client Library
- Deploy the Node.js application with metrics endpoint configured into Kubernetes cluster
- Configure Prometheus to scrape this exposed metrics and visualize it in Grafana Dashboard


---


## Useful CLI commands


### Deploy Microservice in EKS
    eksctl create cluster
    kubectl create namespace online-shop
    kubectly apply -f ./config-microservices.yaml -n online-shop

### Optional for Linode
    chmod 400 ./online-shop-kubeconfig.yaml
    export KUBECONFIG=./online-shop-kubeconfig.yaml


### Deploy Prometheus Operator Stack
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    kubectl create namespace monitoring
    helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
    helm ls

[Link to the chart: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack]

### Check Prometheus Stack Pods
    kubectl get all -n monitoring

### Access Prometheus UI
    kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring &

### Access Grafana
    kubectl port-forward svc/monitoring-grafana 8080:80 -n monitoring &
    user: admin
    pwd: prom-operator

### Trigger CPU spike with many requests

##### Deploy a busybox pod so we can CURL our application 
    kubectl run curl-test --image=radial/busyboxplus:curl -i --tty --rm

##### Create a script which CURLs the application endpoint. The endpoint is the external loadbalancer service endpoint
    for i in $(seq 1 10000)
    do
      curl ae4aee0715edc46b988c6ce67121bf57-1459479566.eu-west-3.elb.amazonaws.com > test.txt
    done


### Access Alert manager UI
    kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-alertmanager 9093:9093 &

#### Create CPU stress
    kubectl delete pod cpu-test; kubectl run cpu-test --image=containerstack/cpustress -- --cpu 4 --timeout 60s --metrics-brief


### Deploy Redis Exporter
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo add stable https://charts.helm.sh/stable
    helm repo update

    helm install redis-exporter prometheus-community/prometheus-redis-exporter -f redis-values.yaml
