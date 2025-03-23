#!/bin/bash

### Exercise:
### Write a bash script using Vim editor that installs the latest java version
### and checks whether java was installed successfully by executing a java -version command.
### Checks if it was successful and prints a success message, if not prints a failure message.

# VARS
PACKAGE_NAME=$1
CHECK_COMMAND="java -version"

if [ -z "$1" ]
then
  echo "Arguments are null."
  exit
else
  apt update
  apt install "$PACKAGE_NAME" -y
fi

$CHECK_COMMAND && echo "Java installed successfully." || echo "Java not installed."
