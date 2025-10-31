                                                                                                                                                                                                                                                                                                                                                                                                                                        #IC 1st class Shopping List Manager

shopping_list = []


while True:
    action = input("\nChoose an action: add = 1, remove= 2 , view =3 , or exit = 4: ")

    if action == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f'"{item}" added to the list.')
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")

    elif action == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f'"{item}" removed from the list.')
        else:
            print(f'"{item}" not found in the list.')
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")

    elif action == "3":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    elif action == "4":
        print("Exiting Shopping List Manager. Goodbye!")
        running = False

    else:
        print("Invalid action. Please choose add, remove, view, or exit.")
