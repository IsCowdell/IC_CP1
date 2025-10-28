#IC 1st combat

import random
enemy = "HGUHSIUhgUHSDU"
enemy_health = 45
enemy_hit = 23
enemy_defense = 21
incombat = True
username = input("What is your username")

def playerturn():
 global health, strength, enemy_health, incombat, enemy_hit, enemy_defense#my dear sweet brother helps me  so much
 print("What would you like to do?")
 print("1. Normal attack")
 print("2. Wild attack")
 print("3. Drink a healing potion (gain 6 health)")
 print("4. Flee (or at least try)")
 action = int(input())
 if action == 1:
     print("You do a normal attack")
     attk = strength + random.randint(0,20)
     if attk > enemy_defense:
         enemy_health -= attk
         print("Attack success, enemy health:", enemy_health)
     else:
         print("Attack Failed")

 elif action == 2:
     print("You do a wild attack")
     health -= random.randint(0,5)
     print("health now", health)
     attk = strength + random.randint(0,20) * 2
     if attk > enemy_defense:
         enemy_health -= attk
         print("Attack success, enemy health:", enemy_health)
     else:
         print("Attack Failed")

 elif action == 3:
     print("You drank a healing potion")
     health += 9
     print("Your health is now", health)

 elif action == 4:
     print("You try to flee")
     if random.randint(0,10) >= 5:
         print("You escaped!")
         incombat = False
     else:
         print("You failed. Run faster next time")

def monsterturn():
    global health, enemy_health, strength, talent
    print("Monster Attacks you")
    attk = enemy_hit + random.randint(0,20)
    if attk > talent:
        health -= attk
        print("Monster attacked you. Your health is now", health)
    else:
        print("Monster Attack failed")

character = input(f"If you want to be a mage press 1 thief press 2 and dora press 7 and rat 5: ")

if character == "1":
    print("your a mage")
    print("this is your stats")
    print("this is your health = 20 strength = 5 combat = 12 and talent is 2")
    health = 20
    combat = 12
    talent = 2 
    strength = 5
elif character == "2":
     print("your a thief")
     print("this is your stats strength = 2 combat = 3 and talent = 24 health = 22")
     strength = 2
     combat = 3 
     talent = 24
     health = 22 
elif character == "7":
     print("you are dora")
     print("this is your stats strength = 70 combat = 57 talent = 78 and healt is 67")
     strength = 70
     combat = 57
     talent = 78
     health = 67
elif character == "5":
     print("you are a rat")
     print('you got stepped on')
     incombat = False          
if incombat:
     print("You are being attacked by", enemy)
     if random.randint(0,1) == 1:
          print("You Go First")
          turn = True
     else:
          print("Monster Goes First")
          turn = False

while incombat:
     if turn == True:
      playerturn()
      turn = False

     else:
      monsterturn()
      turn = True

     if health <= 0:
         incombat == False
         print("You lose")
         break
     
     if enemy_health <= 0:
         incombat == False
         print("You Win")
         break
      
    
    
