#IC 1st rock_paper_scissors

import random

running = True

while running:
    user_input = input("choose rock, paper,scissors")
    rock = 1
    paper = 3
    scissors = 2 
    roll =  random.randint(1,3)

    if roll == scissors:
       print("I got scissors")
       print("You guys tied!")
    elif roll < scissors :
            print("I got paper")
            print("Aw, dang it you won")
    elif roll > scissors:
            print("I got rock")
            print("yay, I won")
    else: 
            ("do you want to quit? 1 is yes, 2 is no")
            if quit == 1:
                break

else:
        print("your input is invaild")
