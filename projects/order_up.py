#IC 1st order up
#importing prints
import pprint




#creating a dctornary for drinks
drinks = {
    'coke' : 1,
    'water' : 13,
    'sprite' : 3.99,
    'apple juice' : 70
          }
#making it print very pretty 

pprint.pprint(f"this is our drinks {drinks}")

#defing the side dishes with prices 
side_dishes = {
    'fries' : 10,
    'salad' : 23,
    'soup' : 5,
    "rice" : 2
}
#time to print them very pretty
pprint.pprint(f"this is our side dishes{side_dishes}")
#defing main dishes and price
main_dishes = {
    'hamburger' : 5,
    'pasta' : 12,
    'steak' : 1,
    'slop' : 300
}
#more pretty printing 
pprint.pprint(f"this is our main dishes{main_dishes}")
#creating order so they can fill it up
order = []





#letting user choose what they want for their drink and adding it to their order

drink_choice = input("choose what you want for your drink: ").lower().strip()
if drink_choice in drinks: 
    print("We have that drink")
    drinkprice =  drinks[drink_choice]
    order.append(drink_choice)
    print(f"this is the price of your drink ${drinkprice}")

    print(f"this is order so far {order}")
else:
    print("we dont have that drink")




#letting user choose what they want for their main dish 
main_choice = input("choose what you want for your main dish: ").lower().strip()

if main_choice in main_dishes:
    print("we have that dish")
    mainprice =  main_dishes[main_choice]
    print(f"This is the price of your main dish ${mainprice}")

    order.append(main_choice)
    print(f"this is order so far {order}")
else:
    print("we don't have that dish try again")

#asking user what they want for their side dish
sidedish1 = input("choose first side dishes: ").lower().strip()

if sidedish1 in side_dishes:
 print("we have that dish")
 side1price =  side_dishes[sidedish1]
 print(f"This is the price of your side dish ${side1price}")
 order.append(sidedish1)
 print(f"this is order so far {order}")
else:
    print("we don't have that dish try again")
sidedish = input("choose second side dishes: ").lower()
#setting up what they want for their second dish 
if sidedish in side_dishes:
 print("rice we have that dish")
 side2price =  side_dishes[sidedish]
 print(f"This is the price of your side dish ${side2price}")
 order.append(sidedish)
 print(f"this is order so far {order}")
else:
     print("we don't have that dish try again")
    

#calucating final cost
finalcost = (side1price + side2price + drinkprice + mainprice)
#telling user final cost
print(f"this is your final order{order} and the final cost ${finalcost} ")