def buildJar() {
    echo "Building jar file..."
    sh "mvn package"
}

def buildDockerImage() {
    echo "Building docker image..."
    withCredentials([usernamePassword(credentialsId: "dockerhub-repo", passwordVariable: "PASSWORD", usernameVariable: "USERNAME")]) {
    sh "docker build -t jimsemara/java-maven-app:2.0 ."
    sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
    sh "docker push jimsemara/java-maven-app:2.0"
    }
}

def testApp() {
    echo "Testing the application..."
}

def deployApp() {
    echo "Deploying the application..."
}

return this