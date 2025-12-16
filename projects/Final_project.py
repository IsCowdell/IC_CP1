import random

mental = 80 
health = 100 
strength = 50 

gilbert_health = 200
gilbert_strength = 10
conductor_health = 200 
conductor_strength = 20
shiny_strength = 10
shiny_health = 40 

inventory = []

fork = "fork"
roasted_crab = "roasted_crab"
dollar_bill = "dollar_bill"

items = [fork, roasted_crab, dollar_bill]

damage = 20
damage1 = 40

FORK_STRENGTH_BONUS = 20
CRAB_HEALTH_BONUS = 20
BILL_HEALTH_BONUS = 20

def enemy_fight(strength):
    
    print("\nshiny attacks you")
    attk = shiny_strength + random.randint(0, 20)
    
    if attk > strength:
        health_loss = attk
        health -= health_loss
        print(f"Shiny attacked you. Your health is now {health}")
    else:
        print("Monster attack failed")

def fight(inventory, fork, strength, health, roasted_crab, dollar_bill, gilbert_health): 
    
    print("Gilbert")
    print(" are you ready to fight?")
    print("you have three different attacks")
    
    temp_strength = strength
    temp_health = health

    print(f"But first do you want to use anything in your {inventory}")
    use_item = input("Do you want to use an item? (yes/no): ").lower().strip()
    
    if use_item == "yes":
        if fork in inventory:
            temp_strength += FORK_STRENGTH_BONUS
            print(f"your strength is now  {temp_strength}")
        if roasted_crab in inventory:
            temp_health += CRAB_HEALTH_BONUS
            print(f"your health is now  {temp_health}")
        if dollar_bill in inventory:
            temp_health += BILL_HEALTH_BONUS
            print(f"your health is now  {temp_health}") 
    else:
        print("you have nothing in your inventory")
    
    print("user choose your attacks ")
    print("attack 1 will be smack hard (20 dmg)\n attack 2 will be smack harder (40 dmg)\nattack 3 is kick hard (30 dmg)\n")
    attack = input("Now choose one: ").lower().strip()
    damage_dealt = 0

    if attack == "attack 1":
        damage_dealt = 20
    elif attack == "attack 2":
        damage_dealt = 40 
    elif attack == "attack 3":
        damage_dealt = 30
    else:
        print("invailad input. No damage dealt.")
        return 
    
    print("attack worked")
    gilbert_health -= damage_dealt
    print(f"Gilbert's health remaining: {gilbert_health}")

def fight2(inventory, fork, strength, health, roasted_crab, dollar_bill, shiny_health): 

    
    
    print(" are you ready to fight?")
    print("you have three different attacks")
    
    temp_strength = strength
    temp_health = health

    print(f"But first do you want to use anything in your {inventory}")
    use_item = input("Do you want to use an item? (yes/no): ").lower().strip()
    
    if use_item == "yes":
        if fork in inventory:
            temp_strength += FORK_STRENGTH_BONUS
            print(f"your strength is now {temp_strength}")
        if roasted_crab in inventory:
            temp_health += CRAB_HEALTH_BONUS
            print(f"your health is now  {temp_health}")
        if dollar_bill in inventory:
            temp_health += BILL_HEALTH_BONUS
            print(f"your health is now  {temp_health}")
    else:
        print("you have nothing in your inventory")

    print("user choose your attacks ")
    print("attack one will be smack hard (20 dmg)\nattack two will be smack harder (40 dmg)\nattack three is kick hard (30 dmg)\n")
    attack = input("Now choose one: ").lower().strip() 
    damage_dealt = 0
    
    if attack == "attack one":
        damage_dealt = 20
    elif attack == "attack two":
        damage_dealt = 40 
    elif attack == "attack three":
        damage_dealt = 30
    else:
        print("invailad input. No damage dealt.")
        return 
    
    print("attack worked")
    shiny_health -= damage_dealt
    print(f"Shiny's health remaining: {shiny_health}")


def leave(mental, damage):

    print("\nyou go to leave and *crash* ")
    print("don gets in your way asking to play a game.")
    print("you could yk end him but he is just a kid")
    print("You HAVE to play a game with him")
    print(" you are now playing rock or scissors no paper")
    
    choose = input('choose "rock" or "scissors" ').lower().strip()
    don_choice = random.choice(["rock", "scissors"])

    if choose == don_choice:
        print(f"It's a tie! Don chose {don_choice}.")
    elif (choose == "rock" and don_choice == "scissors") or \
         (choose == "scissors" and don_choice == "rock"):
        
        print(f"You Won! Don chose {don_choice}.")
        print(" Don gets mad and cries")
        print("cries get unbearable")
        print("you wonder what you can do to make them stop")
        print("you look down at your hands wondering if they could.... its just a kid.")
        print("the cries just stop you look down his neck in your hands.")
        mental -= damage
        print(f"Your mental state is {mental} low get it up")
    else:
        print(f"Don won! He chose {don_choice}.")
        print("He follows you around yelling try harder")


def dinning_room(fork, inventory):

    
    print("Food is stacked everywhere it looks soo good but smells horrid")

    print("The conducor walks up and down looking for kids")

    print("He looks over smiles and waves")
    
    if fork in inventory:
        print("you already have this item you dont get it twice")
    else:
        print("there is a fork")
        if input("Do you want to to grab it? yes or no: ").lower().strip() == "yes":
            inventory.append(fork) 
            print("You now have a fork in inventory")
        else:
            print("wow you didn't want a fork.")

def family_car(mental, damage, inventory):
  
    print("right now you are in the family car")
    print("the room is empty but a bed the bed does nothing")
    leaver_room = input("do you want to leave the room or touch the bed?").strip().lower()
    if leaver_room == "touch the bed":
        print("you are in the secret tunnel")
        secret_tunnel(mental, damage, inventory)
    else:
        print("you leave the room")
        return

def secret_tunnel(mental, damage, inventory):
    print("Secret Tunnel")
    sercet_choice = input("you found Henry Hermit Crab do you want to pet him or countine foward:").strip().lower()
    if sercet_choice == "pet him":
        if roasted_crab in inventory:
            print("Henry runs away! You already have a roasted crab.")
        else:
            print(f" you got a roasted crab it can increase your heath by {CRAB_HEALTH_BONUS} points ")
            print(" when the option is given to you open your invertory by pressing 1")
            inventory.append(roasted_crab)
            mental -= damage
            print(f"your mental state is now {mental} make sure it doesn't get to low like 20")

    elif sercet_choice == "continue foward":
        print("you got out of the tunnel you are in the play area")
        play_room(mental, damage, dollar_bill, inventory)

    else:
        print("incorrect value")
        return
    

def play_room(mental, damage, dollar_bill, inventory):
    
  
    print("You enter a darkish yellow room with a smell of apple sauce and tears")
    print("there is a ball pit looking deeper than your sorrows(ik you have a lot)\n and a slide looking higher than your dreams")
    play_choice = input("where to the ball pit or slide:").strip().lower()
    if play_choice == "slide":
        print("wow you went down the slide")
        leave(mental, damage)
    elif play_choice == "ball pit":
        print("you jump into the pit you can just smell the amount of socks in it" )
        ball_pitchoice = input("you can jump out or stay in").strip().lower()
        if ball_pitchoice == "jump out":
            print("you get out")
            leave(mental, damage)
        else:
            print("you swim around and a find a dollar")
            if dollar_bill not in inventory:
                if input("keep it yes or no:").lower().strip() == "yes":
                    inventory.append(dollar_bill)
                    print(f"you added a dollar into your inventory {inventory}")
                    leave(mental, damage)
                else:
                    leave(mental, damage)
            else:
                print("You already have this item you dont get it twice")
                leave(mental, damage)
    else:
        print("Invalid choice. Leaving the play room.")


def coal_car(mental, damage):

    print(" This is the only place you can get your mental health back vist often")
    print("coal stacked as tall as much money I have (so lots)")
    mental += damage
    print(f" you got {damage} added onto your mental state make sure it doesn't go lower than 20. Current mental: {mental}")

def watching_car():
    
    print("you just watch people consatnly walk by")
    print("first Mrs. Pteranodon walks by")
    print("and then Mr Pteranodon")
    print("and after that King Cryolophosaurus")


def habit_car_water(inventory, fork, strength, health, roasted_crab, dollar_bill, shiny_health, shiny_strength):
    

    print("There is water every where\n it makes it so humid you think your socks are wet( like florida)")
    print("Shiny flies over head every other second shreching and yelling")
    
    if shiny_health > 0:
        print("shiny lands time to fight")
        while shiny_health > 0 and health > 0:
            fight2(inventory, fork, strength, health, roasted_crab, dollar_bill, shiny_health)
            if shiny_health <= 0:
                print("Shiny has been defeated!")
                break
            enemy_fight(strength) 
        
        if health <= 0:
            lose()
    else:
        print("Shiny is already defeated. The car is peaceful.")


def habit_forest_car(damage, mental):

    
    print("you are in the forest car it is covered in trees head to toe the air smellys musty")
    print("its dead slient you slowly wonder what else is dead in there")
    print("you start seeing stars and decide its best to leave.")
    mental -= damage
    print(f"The eerie atmosphere lowered your mental state by {damage}. Current mental: {mental}")

def boss_battle(health, mental, damage, damage1, strength):
 

    print("gilbret screams many people flood in")
    print("he takes a swing")
    
    if mental <= 40:
        print("then he hits you and you lose 40 health")
        health -= damage1
    else:
        print("he misses but goes again")
        
    if strength < 25: 
        print("he hits you and you lose 20 health")
        health -= damage
    else:
        print("he misses but goes again")
    
    print(f"Your health is now {health}")
    return health

def conductor_car(health, damage, strength, inventory, fork, roasted_crab, dollar_bill, gilbert_health):
    
   
    print("you have entered the conductor car but he isn't in there strange")
    print("something starts cackling in the corner i have been watching you something says")
    print("you look behind you and see.........")
    print("glibert")
    print("he is so tiny you could defiently fight him")
    
    if gilbert_health <= 0:
        print("Gilbert is already defeated. The car is empty.")
        return health

    ftboss = input("Fight? yes or no:").strip().lower()
    if ftboss == "no":
        print("You choose not to fight and leave")
        return health
    
    if ftboss == "yes":
        while health > 0 and gilbert_health > 0:
            fight(inventory, fork, strength, health, roasted_crab, dollar_bill, gilbert_health)
            if gilbert_health <= 0:
                win()
                return health
            
            health = boss_battle(health, mental, damage, damage1, strength)
        
        if health <= 0:
            lose()
            return health
    
    print("Invalid choice. Leaving the car.")
    return health
    
rooms = ["dinning_room","play_room","habit_car_water","habit_forest_car","watching_car","family_car","coal_car","conductor_car",]

def reset_game():
   
    health = 100
    mental = 80
    strength = 50

    shiny_health = 40
    gilbert_health = 200

    inventory.clear()
    

def play_again():
    choice = input("\nPlay again? (yes/no): ").lower()
    if choice == "yes":
        reset_game()
        start_game()
    else:
        print("Thanks for playing.")
        exit()

def win():
    print("\nYOU WON THE GAME")
    print("Gilbert has been defeated.")
    play_again()

def lose():
    
    print("\nYOU LOST")
    print("Your journey ends on the Dinosaur Train.")
    play_again()


def start_game():
    

    if gilbert_health <= 0:
        win()
        return
    elif health <= 0:
        lose()
        return

    print("your still alive")
    while health > 0 and gilbert_health > 0:
        print(f"Current Stats: Health={health}, Mental={mental}, Strength={strength}")
        print(f"Inventory: {inventory}")
        print(f"Available rooms: {list(rooms)}")
        
        room = input("What room do you want to go to? Do not put underscores: ").strip().lower()
        
        if room == "dinning room":
            print(f"Navigating to {room}...")
            dinning_room(fork, inventory)
        elif room == "play room":
            print(f"Navigating to {room}...")
            play_room(mental, damage, dollar_bill, inventory)
        elif room == "habit car water":
            print(f"Navigating to {room}...")
            habit_car_water(inventory, fork, strength, health, roasted_crab, dollar_bill, shiny_health, shiny_strength)
        elif room == "habit forest car":
            print(f"Navigating to {room}...")
            habit_forest_car(damage, mental)
        elif room == "watching car":
            print(f"Navigating to {room}...")
            watching_car()
        elif room == "family car":
            print(f"Navigating to {room}...")
            family_car(mental, damage, inventory)
        elif room == "coal car":
            print(f"Navigating to {room}...")
            coal_car(mental, damage)
        elif room == "conductor car":
            print(f"Navigating to {room}...")
            conductor_car(health, damage, strength, inventory, fork, roasted_crab, dollar_bill, gilbert_health)
        else:
            print(f"Sorry, '{room}' is not a recognized room. Please choose from the list above.")
    
    if health <= 0:
        lose()
    elif gilbert_health <= 0:
        win()

print("Basically it went off course and the gilbert turned everything evil and you as the viewer were forced to get to the train conductor so the final boss is the gilbert.. Each train cart is a different combat room and has their individual monsters based on the show like shiny. ")
print("hi my name is buddy I will guide you")

reset_game()
start_game()


#Ms larose if your seeing this I would like to say thank you for all that you do because I didn't realize how much i would like coding until i was forced to talk this class 
# it was ngl kinda life changing i didn't know their was another way to express myself 
# and i would just like to thank you for everything.