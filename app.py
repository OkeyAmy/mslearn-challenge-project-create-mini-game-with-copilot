from calendar import c
import random
from re import U
from turtle import end_fill

choice = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_input = input('Enter your choice: ').lower()
    while user_input not in choice:
        print("Select a valid choice:")
        user_input = input('Enter your choice ' + str(choice) + ": " ).lower()
    return user_input

print("Your choice is: " + get_user_choice())

def get_computer_choice():
    computer_input = random.choice(choice)
    return computer_input

print("Computer choice is: " + get_computer_choice())

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
        user_choice == 'paper' and computer_choice == 'rock' or \
        user_choice == 'scissors' and computer_choice == 'paper':
        return "You won"
    else:
        return "Computer Won"
    

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(determine_winner(user_choice,computer_choice))

play_game()