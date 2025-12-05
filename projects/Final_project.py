#IC 1st Dinosaur train final project 
# import random
import random
# mental = 100
mental = 100 
#health = 100
health = 100 
#strength = 50 
strength = 50 
# charcters 
# gilbert = 500 health and strength = 300 
gilbert_health = 500
gilbert_strength = 300 
# conductor = health 200 and strength = 20
conductor_health = 200 
conductor_strength = 20
# Shiny = health 50 and strength = 10
shiny = 50 
shiny_strength = 10
# list for inverntory
inventory = []
# making a list for all of the rooms
rooms = []
# don stats
#strength = 24
don_strength = 24
#health = 80 
health = 80
#define fork 
fork = strength + 20
roasted_crab = health + 20 
dollar_bill = health + 20 

#buddy 
# this will be your guide and explain each room to you 
# print hi my name is buddy I will guide you
print("hi my name is buddy I will guide you")


# define the function to see if user picekd up item 
def item_pickup():
# if item in inventory 
    
# do not show user item.

# define the function enemy fight: 
def enemy_fight():
    #global health, enemy_health, strength, enemy health
    global health, shiny_strength, shiny, strength
    #show the user("Monster Attacks you")
    print("shiny attacks you")
    #attk = enemy_hit + random.randint(0,20)
    attk = shiny + random.randint(0,20)
    #if attk > stength :
    if attk > strength:
        #health -= attk
        health -= attk
        #print("Monster attacked you. Your health is now", health)
        print("Shiny attacked you. Your health is now",health)
    #else:
    else:
        #show the user ("Monster Attack failed")
        print("Monster attack failed")

#  define the function fight:
def fight(): 
# show the user(are you ready to fight)
    print(" are you ready to fight?")
#  show the user you have three different attacks
    print("you have three different attacks")
# ask the user(f"But first do you want to use anything in your{inventory}")
    print(f"But first do you want to use anything in your{inventory}")
# if user has fork:
    if inventory == fork:
        print(f"your strength is now {strength}")

    if inventory == roasted_crab:
        print(f"your health is now{health}")

    if inventory == dollar_bill:
        print(f"your health is now {health}") 
    else:
        print("you have nothing in your inventory")
# show the user choose your attacks
print("user choose your attacks ")
#attack one will be smack hard 
# attack two will be smack harder
# attack three is kick hard 
# attack one gets minus 20 health 
# attack 2 gets minus 40 health
# atttack 3 gets minus 30 health 
# 

# leave function
def leave():
# and go to *crash*
    print("you go to leave and *crash* ")
# Don gets in your way asking to play a game. 
    print("don gets in your way asking to play a game.")
# You could defiently take this but its just a kid 
    print("you could yk end him but he is just a kid")
# do you want to play a game with him,
    print("You HAVE to play a game with him")
# you are now playing rock or scissors no paper 
    print(" you are now plaing rock or scissors no paper")
# 1 = rock 
    1 = "rock"
#  2 = scissors 
    2 = "scissors"
# show the user " chose one 1 or 2"
    choose = input("choose "1" or "2"")
# if choose = 1 
    if choose == 1:
# print(" You won")
        print("You Won!")
# Don gets mad and cries 
        print(" Don gets mad and cries")
# the cries get unbearable
        print("cries get unbearable")
# ("you wonder what you can do to make them stop")
        print("you wonder what you can do to make them stop")
#(you look down at your hands wondering if they could.... its just a kid.)
        print("you look down at your hands wondering if they could.... its just a kid.")
#(the cries just stop you look down his neck in your hands.)
        print("the cries just stop you look down his neck in your hands.")
#mental - 20 
        mental - 20
#(f"Your mental state is {mental} low get it up)   
        print(f"Your mental state is {mental} low get it up")
# else
    else:
# print("Don won but he doesn't look happy.....")
        print("Don won but he doesn't look happy.....")
# print("He follows you around yelling try harder")
        print("He follows you around yelling try harder")
# call on rooms function



# function for dinning room
def dinning_room():
# food is stacked up until the roof but it smells so bad 
    print("Food is stacked everywhere it looks soo good but smells horrid")
# conductor is walking around the table checking for kids
    print("The conducor walks up and down looking for kids")
# he looks over and waves 
    print("He looks over smiles and waves")
# There is a fork
    print("there is a fork")
# do you want to grab it? y/n 
    input("Do you want to to grab it? yes or no")
# if yes:
    if "yes":
# add to inventory()
        inventory.append(fork) 
# else:
    else:
        print("wow you didn't want a fork.")
# 

# define the function family car 
#right now you are in the family car
# the room is empty but a bed the bed does nothing 
#user choice 
#input("do you want to leave the room or touch the bed")
#if user_choice == "leave room"
# then input("what room do you want to go to dinning room or the play area")
# define the function secret  tunnels 
#else if print("you are in the secret tunnel")
#print(" you found Henry Hermit Crab do you want to pet him or countine foward")
# if pet him then 
# print(" you got a roasted crab it can increase your heath by 10 points ")
# print(" when the option is given to you open your invertory by pressing 1")
# add roasted crab to invetory
# subtract mental state by 20 
# print(f"your mental state is now {mental state} make sure it doesn't get to low like 20")
# if "countine foward"
#show the user you got out of the tunnel you are in the play area
#else
#incorrect vaule send back up 

# defining function play room 
# buddy "You enter a darkish yellow room with a smell of apple sauce and tears"
# there is a ball pit looking deeper than your sorrows(ik you have a lot)
# and a slide looking higher than your dreams
# or you could leave
# user choice(" where to ball pit or slide or leave ") 
# if slide:
# show user wow you went down the slide;
# calling on the function leave()
# else:
#leave()
# if ball pit 
# print(you jump into the pit you can just smell the amount of socks in it )
#(you can jump out)
# if "jump out"
# you get out and (leave function)
# else:
# you swim around and found a dollar 
# (keep it? y\n)
# if yes add to inventory() 
# else 
# leave function()
#
# 
# 
# function for coal car 
# Print(" This is the only place you can get your mental health back vist often")
# print("coal stacked as tall as much money I have")
# mental_state + 20 
# print(" you got 20 added onto your mental state make sure it doesn't go lower than 20")

# function for watching car: 
# you just watch people consatnly walk by
# first Mrs. Pteranodon walks by
# and then Mr Pteranodon 
# and after that King Cryolophosaurus

# function for habit car water 
# There is water every where make it so humid you think your socks are wet
# like florida
#  Shiny flies over head every other second shreching and yelling
#  shiny lands time to fight()
# calling enemy_fight function() 

# function for habit forest car
# show the user(you are in the forest car it is covered in trees head to toe the air smellys musty)
# show the user(its dead slient you slowly wonder what else is dead in there)
# show the user you start seeing stars and decide its best to leave. 
# mental state minus 20 
# 
# function for boss battle 
# show the user( gilbret screams many people flood in)
# (he takes a swing)
# if mental state is lower than 40
# then he hits you and you lose 20 health 
# else;
# he misses but goes again
# if strength is greater than 25 
# he misses but goes again
# else:
#he hits you and you lose 20 health 


# function for conductor car 
# show the user (you have entered the conductor car but he isn't in there strange)
# show the user (something starts cackling in the corner i have been watching you something says)
# show the user(you look behind you and see.........)
# show the user(glibert)
# show the user he is so tiny you could defiently fight him
# calling on fight function and boss battle function. 
# switch bewtween the two
# I DONT KNOW HOW I WILL BUT I WILL
# ask user what room the want to and if room in room list 
# play the function for that room



