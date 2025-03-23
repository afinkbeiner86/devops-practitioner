# Module 6 - Containers with Docker

**Technologies Used:**  
Docker, Docker-Compose, Nexus, Node.js, MySQL, MongoDB, Gradle, Java, Git, DigitalOcean, Linux

### Project Overview
- Create Dockerfile and build image for Node.js application locally
- Run MongoDB and MongoExpress, connect all three containers
- Write docker-compose file to configure and run all three containers
- Create volumes and attach them to the MondoDB Container to persist data
- Setup and run Nexus as a container
- Configure docker-hosted repo with user auth, permissions and endpoint
- Tag and push docker image to Nexus repo

### Exercise
- Create dockerized mysql database and phpadmin, then use docker-compose to configure and run both containers
- Dockerize Java app with gradle and openjdk Docker images, add it to docker-compose
- Implement env-vars into the docker-compose file so that they can be configured with the .env file
- Setup fresh Nexus server running in a docker container
- Create docker-hosted repo and appropriate user authentication
- Build Java app container image and push it to the Nexus docker repo
- Use Docker on another Digital Ocean droplet to login to the Nexus docker repo
- Use the docker-compose and .env file to deploy all three containers
