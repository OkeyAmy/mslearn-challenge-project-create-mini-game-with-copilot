import random

user_name = input("Enter your name: ")
user_name = user_name.capitalize()
print("Hello " +user_name + "\nWelcome to Rock Paper Scissors game!")

score = 0
rounds_played = 0

while True:
    user_input = input("Select rock, paper or scissors: ").lower()
    print("User choice is " + user_input)
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options).lower()
    print("Computer choice is " + computer_choice)

    if user_input not in options:
        print("Invalid input. Try again.")
        continue

    if user_input == computer_choice:
        print("It's a draw!")
        rounds_played += 1

    elif user_input == "rock" and computer_choice == "scissors" or \
            user_input == "paper" and computer_choice == "rock" or \
            user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        score += 1
        rounds_played += 1

    else:
        print("You lose!")
        rounds_played += 1

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(user_name + "\nYou played " + str(rounds_played) + " rounds and your score is " + str(score))
            break

        