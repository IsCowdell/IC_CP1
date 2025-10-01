#IC 1st class Shopping List Manager

shopping_list = []
item = []

while True:
    print ("1 = add to list \n 2 = remove something from list \n 3 = show list \n  4 = ")
    action = ("exit") 

    if action == "1":
        item = str(input("What is the item you want to add "))
        shopping_list.append(item)
        print(f"the item you added was",(item))
    elif action == "2": 
        removal = str(input("what item do you want to get rid of? "))
    elif item == removal:
        shopping_list.remove(item)
        print(f"you removed",(item))
    elif action == "3":
         print(shopping_list)

    elif action == "4":
        break
    else:
        print("that is not a vaild action")