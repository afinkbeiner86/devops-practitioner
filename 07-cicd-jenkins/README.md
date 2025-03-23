# Module 7 - Build Automation & CI/CD with Jenkins

### Project Description
Setup a fully functional Jenkins server and create CI pipeline jobs.  
Leverage practices and technologies learned from the lectures before.

#### 1. Install Jenkins
**Technologies Used:**  
Jenkins, Docker, Nexus, Java, Maven, Git, DigitalOcean, Linux  
  
**Overview**:
- Create Ubuntu Server on DigitalOcean
- Setup Jenkins server as Docker container
- Initialize Jenkins

#### 2. Create CI Pipeline with Jenkinsfile (Freestyle, Pipeline, Multibranch Pipeline)
**Technologies Used:**  
Jenkins, Docker, Nexus, Java, Maven, Git, DigitalOcean, Linux  
  
**Overview**:  
Setup CI pipeline for Java Maven application
- Install build tools (Java, Maven) in Jenkins
- Integrate Docker into Jenkins
- Create credentials in Jenkins for connecting Git repo and Docker registry
- Create different Jenkins job types (Freestyle, Pipeline, Multibranch Pipeline) to...
  - Connect to the application's Git repo
  - Build Java jar file
  - Build Docker image
  - Push to private Docker registry at DockerHub and Nexus Server

#### 3. Create a Jenkins Shared Library
**Technologies Used:**  
Jenkins, Groovy, Docker, Git, Java, Maven  
  
**Overview**:  
Create a Jenkins Shared Library to extract common build logic:
- Create separate Git repository for Jenkins Shared Library
- Create functions in the JSL to use in the Jenkins pipeline
- Integrate and use the JSL in Jenkins Pipeline (globally and for a specific project in Jenkinsfile)

#### 4. Configure Webhooks to trigger CI Pipeline automatically on every change
**Technologies Used:**  
Jenkins, GitLab, Git, Docker, Java, Maven  

**Overview**:  
- Install GitLab Plugin in Jenkins 
- Configure GitLab access token and connection to Jenkins in GitLab project settings
- Configure Jenkins to trigger the CI pipeline, whenever a change is pushed to GitLab

#### 5. Dynamically Increment Application version in Jenkins Pipeline
**Technologies Used:**  
Jenkins, Docker, GitLab, Git, Java, Maven  

**Overview**:  
- Configure CI:
  - Increment patch version 
  - Build Java application and clean old artifacts
  - Build Image with dynamic Docker Image Tag
  - Push Image to private DockerHub repository
  - Commit version update of Jenkins back to Git repository
- Configure Jenkins pipeline to not trigger automatically on CI build commit to avoid commit loop

#### Exercise
**Technologies Used:**  
Jenkins, Docker, Java, Node.js, Git, DigitalOcean, Linux
  
**Overview**:  
Setup CI pipeline for Node.js application
- Install & configure build tools (node) in Jenkins
- Dockerize Node.js app
- Create a complete CI pipeline job in Jenkins for the Node.js app, containing following steps:
  - Increment minor version
  - Run tests
  - Build Docker image
  - Login to DockerHub
  - Push Docker image to DockerHub
  - Commit version bump to remote Git repository
- Deploy and run Docker image to a DigitalOcean droplet
- Create a shared library with all the logic from the previous pipeline job
  - Implement shared library in Jenkinsfile
