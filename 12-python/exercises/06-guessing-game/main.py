"""
EXERCISE 6: Python Program 'Guessing Game'
Write a program that:

runs until the user guesses a number (hint: while loop)
generates a random number between 1 and 9 (including 1 and 9)
asks the user to guess the number
then prints a message to the user, whether they guessed too low, too high
if the user guesses the number right, print out YOU WON! and exit the program
Hint: Use the built-in random module to generate random numbers https://docs.python.org/3.3/library/random.html

Concepts covered: Built-In Module, User Input, Comparison Operator, While loop
"""

import random

number_to_guess = random.randrange(1, 9)
user_guess_input = ""

while user_guess_input != number_to_guess:
    try:
        user_guess_input = input("Guess the magic number from 1 to 9: ")
        if user_guess_input == "exit":
            print(f"Already giving up?")
            raise SystemExit()
        
        user_guess_input = int(user_guess_input)
        
        if user_guess_input == number_to_guess:
            print(f"YOU WON!")
            raise SystemExit()
        elif user_guess_input < number_to_guess:
            print("The magic number is higher than you guessed!")
        elif user_guess_input > number_to_guess:
            print("The magic number is lower than you guessed!")
    
    except ValueError:
        print("Only integers allowed.")