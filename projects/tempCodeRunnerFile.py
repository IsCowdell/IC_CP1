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
         print(