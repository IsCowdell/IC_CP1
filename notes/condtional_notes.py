#IC 1st Conditionals Notes 
import random
player_hp = 20 
player_attack = 5
player_damage = 5
player_defense = 5


monster_hp = 15
monster_attack = 3
monster_damage = 10 
monster_defense = 2 

hit_roll = random.randint(1,20) + player_attack
damage_roll = random.randint(1,8) + player_damage
if hit_roll == 20:
    print("you got a crit! That means you get to roll for damage twice")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_damage 
    print(f"you did {damage_roll-monster_defense} damage")
    monster_hp -= (damage_roll-monster_defense)
elif hit_roll == 1:
    print("You rolled a 1 its a criical failure! Now the monster attacks you!")
    damage_roll = random.randint(1,12) + monster_damage
    player_hp -= (damage_roll - player_defense)
    print(f"the monster rolled{damage_roll} your hp is now {player_hp}")

elif hit_roll + player_attack >= 12:
    print("You have hit! Roll for damage!")
    damage_roll = random.randint(1,8) + player_damage 
    if damage_roll > monster_defense:
        print(f"You did {damage_roll-monster_defense} damage.")
        monster_hp <= (damage_roll-monster_hp)
    else:
        print("you did no damage")
else:
    print("you missed.")


print("Your turn is over")


if True > 0:
    attack_roll = random.randint(1,20) + monster_attack

# comparsion operators >greater than <less than ==equal !=not equal >= greater than or equal to <= less than or equal to
# 