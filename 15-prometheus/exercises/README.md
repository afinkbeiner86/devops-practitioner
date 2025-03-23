### Sources
Java-MySQL App used for the exercises: https://gitlab.com/devops-training3784615/devops-built/-/tree/feature/monitoring

### Context
You and your team are running the following setup in the K8s cluster:

Java application that uses Mysql DB and is accessible from browser using Ingress. It's all running fine, but sometimes you have issues where Mysql DB is not accessible or Ingress has some issues and users can't access your Java application. And when this happens, you and your team spend a lot of time figuring out what the issue is and troubleshooting within the cluster. Also, most of the time when these issues happen, you are not even aware of them until an application user writes to the support team that the application isn't working or developers write you an email that things need to be fixed.

As an improvement, you have decided to increase visibility in your cluster to know immediately when such issues happen and proactively fix them. Also, you want a more efficient way to pinpoint the issues right away, without hours of troubleshooting. And maybe even prevent such issues from happening by staying alert to any possible issues and fixing them before they even happen.

Your manager suggested using Prometheus, since it's a well known tool with a large community and is widely used, especially in K8s environment.

So you and your team are super motivated to improve the application observability using Prometheus monitoring.


#### Exercise 1: Build & Deploy Java Artifact
- Create a K8s cluster
- Deploy Mysql database for your Java application with 2 replicas (You can use the following helm chart: https://github.com/bitnami/charts/tree/master/bitnami/mysql)
- Deploy Java Maven application with 3 replicas that talks to the Mysql DB
- Deploy Nginx Ingress Controller (You can use the following helm chart: https://github.com/kubernetes/ingress-nginx/tree/master/charts/ingress-nginx)
- Now configure access to your Java application using an Ingress rule
You can use the Ansible playbook from Ansible exercises 7 & 8 with a few adjustments to configure this setup.

#### Exercise 2: Start Monitoring your Applications
Note: As you've learned, we deploy separate exporter applications for different services to monitor third party applications. But, some cloud native applications may have the metrics scraping configuration inside and not require an addition exporter application. So check whether the chart of that application supports scraping configuration before deploying a separate exporter for it.

- Deploy Prometheus Operator in your cluster (You can use the following helm chart: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
- Configure metrics scraping for Nginx Controller
- Configure metrics scraping for Mysql
- Configure metrics scraping for Java application (Note: Java application exposes metrics on port 8081, NOT on /metrics endpoint)
- Check in Prometheus UI, that all three application metrics are being collected

#### Exercise 3: Configure Alert Rules
Now it's time to configure alerts for critical issues that may happen with any of the applications.

- Configure an alert rule for nginx-ingress: More than 5% of HTTP requests have status 4xx
- Configure alert rules for Mysql: All Mysql instances are down & Mysql has too many connections
- Configure alert rule for the Java application: Too many requests
- Configure alert rule for a K8s component: StatefulSet replicas mismatch (since Mysql is deployed as a StatefulSet, if one of the replicas goes down, we want to be notified)

#### Exercise 4: Send Alert Notifications
Great job! You have added observability to your cluster, and you have configured your monitoring with all the important alerts. Now when issues happen in the cluster, you want to automatically notify people who are responsible for fixing the issue or at least observing the issue, so it doesn't break the cluster.

- Configure alert manager to send all issues related to Java or Mysql application to the developer team's Slack channel. (Hint: You can use the following guide to set up a Slack channel for the notifications: https://www.freecodecamp.org/news/what-are-github-actions-and-how-can-you-automate-tests-and-slack-notifications/#part-2-post-new-pull-requests-to-slack)
- Configure alert manager to send all issues related Nginx Ingress Controller or K8s components to K8s administrator's email address.
Note: Of course, in your case, this can be your own email address or your own Slack channel.

#### Exercise 5: Test the Alerts
Of course, you want to check now that your whole setup works, so try to simulate issues and trigger 1 alert for each notification channel (Slack and E-mail).

For this, you can simply, kubectl delete one of the stateful set pods, or Mysql pods or try accessing your java applications on a /path-that-doesnt-exist etc.
