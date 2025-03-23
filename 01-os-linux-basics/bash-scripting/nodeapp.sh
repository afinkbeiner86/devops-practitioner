#!/bin/bash
###
### EXERCISE 6: Bash Script - Start Node App
### Write a bash script with following logic:
###
### Context: We have a ready NodeJS application that needs to run on a server. The app is already configured to read in environment variables.
###
### Install NodeJS and NPM and print out which versions were installed
### Download an artifact file from the URL: https://node-envvars-artifact.s3.eu-west-2.amazonaws.com/bootcamp-node-envvars-project-1.0.0.tgz.
### Hint: use curl or wget
### 1. Unzip the downloaded file
### 2. Set the following needed environment variables: APP_ENV=dev, DB_USER=myuser, DB_PWD=mysecret
### 3. Change into the unzipped package directory
### 4. Run the NodeJS application by executing the following commands:  npm install and node server.js
###
### Notes:
### Make sure to run the application in background so that it doesn't block the terminal session where you execute the shell script
### If any of the variables is not set, the node app will print error message that env vars is not set and exit
### It will give you a warning about LOG_DIR variable not set. You can ignore it for now.

#VARS
URL="https://node-envvars-artifact.s3.eu-west-2.amazonaws.com/bootcamp-node-envvars-project-1.0.0.tgz"
DST_DIR="/srv"
FILE_PATH="$DST_DIR/bootcamp-node-envvars-project-1.0.0.tgz"
SVC_USER=myapp

# Read user input to confire log directory as absolute path
read -p "Please set the LOG_DIRECTORY (absolute path, default=/var/log/nodejsapp): " LOG_DIRECTORY
if [ -z $LOG_DIRECTORY ]
then
  LOG_DIRECTORY=/var/log/nodejsapp
  if [ ! -d "$LOG_DIRECTORY" ]
  then
    echo "Creating log directory: $LOG_DIRECTORY"
    mkdir -p $LOG_DIRECTORY
  else
    echo "Log directory already exists."
  fi
elif [ -d "$LOG_DIRECTORY" ]
then  
  echo "Log directory already exists."
else
  echo "Creating log directory: $LOG_DIRECTORY"
  mkdir -p $LOG_DIRECTORY
fi

# Update apt cache and install requirements
apt update
apt install -yy wget lsof npm nodejs

# Print installed versions on NodeJS and npm
echo "NodeJS $(nodejs -v) installed." || echo "NodeJS installation failed."
echo "npm $(npm -v) installed." || echo "npm installation failed."

# Fetch NodeJS app
if [ -f "$FILE_PATH" ] 
then
  echo "File already downloaded."
else
  wget -q -P "$DST_DIR"/ "$URL"
  tar -xf "$FILE_PATH" -C "$DST_DIR"
fi

# Add service user and change ownership of log dir and nodejs files
useradd -m $SVC_USER
chown -R :$SVC_USER $DST_DIR/package/ ; chmod -R g+rwx $DST_DIR/package/
chown -R :$SVC_USER $LOG_DIRECTORY ; chmod -R g+rwx $LOG_DIRECTORY

# Setup environment and start nodejs app as service user
su -c "
    export APP_ENV=dev && 
    export DB_PWD=mysecret && 
    export DB_USER=myuser && 
    export LOG_DIR=$LOG_DIRECTORY && 
    cd $DST_DIR/package && 
    npm install && 
    node server.js &" $SVC_USER

# Wait for the app to start, print service and port of nodejs app
sleep 15
echo
echo "NodeJS app running as process:   $(ps aux | grep "node server.js" | grep -v grep)"
# Gotta use this "su -c" 'hack' here because of a problem with lsof and containers: https://github.com/lxc/lxc/issues/1059
echo "NodeJS app running on port:    $(su -c "lsof -i" $SVC_USER | grep node | awk '{ print $8$9$10 }')"
echo
