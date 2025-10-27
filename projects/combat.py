#IC 1st combat

import random
enemy = "HGUHSIUhgUHSDU"
enemy_health = 45
enemy_hit = 23
talentenemy = 21
combat = 11
username = input("What is your username")

character = input(f"If you want to be a mage press 1 thief press 2 and dora press 7 and rat 5: ")

if character == "1":
    print("your a mage")
    print("this is your stats")
    print("this is your strength = 5 combat = 12 and talent is 2")
    combat = 12
    talent = 2 
    strength = 5
else:
   
    if character == "2":
         print("your a thief")
         print("this is your stats strength = 2 combat = 3 and talent = 24 health = 22")
         thiefstrength = 2
         thiefcombat = 3 
         talentthief = 24
         health = 22 
    else:
        
         if character == "7":
              print("you are dora")
              print("this is your stats strength = 70 combat = 57 talent = 78 and healt is 67")
              dorastrength = 70
              combatdora = 57
              talent = 78
              health = 67
         else:
          
              if character == "5":
                    print("you are a rat")
                    print('you got a stepped on')
                    
              else: 
                    print()

turn_counter = random.randint(1,20)
fighting = input("do you want to fight a monster yes or no: ")
if fighting == "yes":
     print("you are going against HGUHSIUhgUHSDU")
     print("let see if you go first")
     if turn_counter >= 10:
            print("you go first")
     else:
            print("monster goes first")
                 
            
        
      
    
    
