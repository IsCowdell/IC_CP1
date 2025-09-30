#IC 1st Fix game

import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False

    while not game_over:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            # Bug 1: Runtime Erro because the input could be a letter
           
            # Why: Prevents crash when user enters something that can't be converted to int
            print("Please enter a valid number.")
            continue

        attempts += 1  # Bug 2: Logic Error - attempts were never started 
        
        # Why: Without adding it, the game never reaches max_attempts

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")

        # Bug 3: Logic Error - why did it have the contuine 
        
        # Why: It will mess it up becuase it might go forever?

    print("Game Over. Thanks for playing!")

start_game()
