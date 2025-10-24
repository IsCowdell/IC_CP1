#IC 1st combat

import random
mage = 1
thief = 2
dora = 7 
username = input("What is your username")

character = input(f"If you want to be a mage press 1 if you want to be a thief press 2 and if you want to be dora press 7: ")

if character == "1":
    print("your a mage")
    print("this is your stats")
    print("this is your strength = 5 combat = 12 and talent is 2")
    combat = 12
    talent = 2 
    strength = 5
else:
    print()
    if character == "2":
         print("your a thief")
         print("this is your stats strength = 2 combat = 3 and talent = 24 health = 22")
         thiefstrength = 2
         thiefcombat = 3 
         talentthief = 24
         health = 22 
    else:
         print()

fighting = input("do you want to fight a monster yes or no: ")
if fighting == "yes":
     print("you are going against HGUHSIUhgUHSDU")
     print("let see if you go first")
     if random.randint <= 10:
            print("you go first")
            attack = input("what do you want to do 1 or 2")
            if attack == "1":
                 print("wow did a magic twirly took off 35 of his health he has 22 left")
                 print("monster turn")
            else:
                 print("you did a flying mokey")
                 print("YOU KILLED THE MONSTER!")
     else:
            print("monster goes first")

        
    
