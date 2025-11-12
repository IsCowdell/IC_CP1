#IC 1st order up
yes = True 
drinks = {
    'coke' : 1,
    'water' : 13,
    'sprite' : 3.99,
    'apple juice' : 70
          }


side_dishes = {
    'fries' : 10,
    'salad' : 23,
    'soup' : 5,
    "rice" : 2
}

main_dishes = {
    'hamburger' : 5,
    'pasta' : 12,
    'steak' : 1,
    'slop' : 300


}

order = []

print("this is our menu ")
print(side_dishes,main_dishes,drinks)



drink_choice = input("choose what you want for your drink: ").lower().strip()
if drink_choice in drinks: 
    print("We have that drink")
    order.append(drink_choice)
    print(f"this is order so far {order}")
else:
    print("we dont have that drink")




main_choice = input("choose what you want for your main dish: ").lower()

if main_choice in main_dishes:
    print("we have that dish")
    order.append(main_choice)
    print(f"this is order so far {order}")
else:
    print("we don't have that dish try again")

sidedish1 = input("choose first side dishes: ").lower()

if sidedish1 in side_dishes:
    print("we have that dish")
    order.append(sidedish1)
    print(f"this is order so far {order}")
else:
    print("we don't have that dish try again")



sidedish = input("choose second side dishes: ").lower()

if sidedish in side_dishes:
    print("we have that dish")
    order.append(sidedish)
    print(f"this is order so far {order}")
else:
    print("we don't have that dish try again")


final_order = order


print(f"this is your final order{order} and ")