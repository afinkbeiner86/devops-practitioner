#!/bin/bash

###EXERCISE 3: Bash Script - User Processes
### Write a bash script using Vim editor that checks all the processes running for the current user (USER env var)
### and prints out the processes in console.

### EXERCISE 4: Bash Script - User Processes Sorted
### Extend the previous script to ask for a user input for sorting the processes output either
### by memory or CPU consumption, and print the sorted list.

### EXERCISE 5: Bash Script - Number of User Processes Sorted
### Extend the previous script to ask additionally for user input about how many processes to print. 
### Hint: use head program to limit the number of outputs. 

while true
do
  read -p "Sort by MEM or CPU? " SORT_OPTION
  read -p "Number of processes to display? " PROC_NUMBER
  if [ -z $SORT_OPTION ] && [ -z $PROC_NUMBER ]
  then
    echo "Processes for User: $USER"
    ps aux | grep $USER
    break
  elif [ $SORT_OPTION = "MEM" ] && [ -z $PROC_NUMBER ]
  then
    ps aux --sort -pmem | grep $USER
    break
  elif [ $SORT_OPTION = "MEM" ] && [ -n $PROC_NUMBER ]
    then
    ps aux --sort -pmem | grep $USER | head -n $PROC_NUMBER
    break
  elif [ $SORT_OPTION = "CPU" ]  && [ -z $PROC_NUMBER ]
  then
    ps aux --sort -pcpu | grep $USER
    break
  elif [ $SORT_OPTION = "CPU" ]  && [ -n $PROC_NUMBER ]
  then
    ps aux --sort -pcpu | grep $USER | head -n $PROC_NUMBER
    break
  else
    echo "Wrong input, please run it again."
  fi
done