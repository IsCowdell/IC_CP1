#IC 1st class Shopping List Manager

shopping_list = []

while True:
    print ("1 = add to list \n 2 = remove something from list \n 3 = show list \n  4 = ")
    action = ("exit") 
    
    if action == "1":
        item = input("What is the item you want to add ")
        shopping_list.append(item)
        print(f"the item you added was",(item))
    elif action == "2": 
        remove = input("what item do you want to get rid of? ")
    if item == remove:
        shopping_list.remove(item)
        print(f"you removed",(item))
    elif action == "3":
         print(shopping_list)

    elif action == "4":
        break
    else:
        print("that is not a vaild action")