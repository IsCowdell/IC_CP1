#IC 1st rock_paper_scissors

import random

your_score = 0
running = True

while running:
    user = input("choose rock, paper, scissors or quit: ")
    roll = random.choice(["rock", "paper", "scissors"])
    if user == "quit":
        break
    elif user == "rock" or user == "paper" or user == "scissors":
        print(f"I got {roll}")
        if roll != user:
           if (roll == "rock" and user == "paper") or (roll == "paper" and user == "scissors") or (roll=="scissors" and user=="rock"):
                print("You won")
                your_score += 1
                print(f"Your Score: {your_score}")
           else:
                print("You lost!")
                print(f"Your Score: {your_score}")

        else:
                print("We tied!")
                print(f"Your Score: {your_score}")
    else:
        print("invaild input try again")    

    
           

       
