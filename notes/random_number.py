#IC 1st Random number notes 
import random 
name = input("What is your character name?\n").strip().title()

#Generate Stat Options
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

#Telling user the stat choices 
print(f"Your stat options are: {stat_one},{stat_two},{stat_three},{stat_four},{stat_five},{stat_six},{stat_seven},")

#Set stats
strength = input("Which stat do you want as your strength: \n") +2


print(random.random())
print(random.randint(1,20))
print(f"this is a random number from 1-20: {random.randint(1,20)}")