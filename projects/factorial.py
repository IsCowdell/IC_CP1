# IC 1st 
# and sadly jacob 
# action = true

action = True

# while action:
while action:
    # usernum is asked "what number do you want to set a factorial number for,? all decimals will be rouhoer" had to make sure I add in the great spelling
    user_input = input("what number do you want to set a factorial number for? all decimals will be rounded down: ")
#all of these is the orignal spelling btw
    try:
        # actions = True : counter = 1
        action = True
        counter = 1

        # try int(user_num):
        user_num = int(float(user_input))  # convert to int, rounding down decimals

        if user_num < 0:
            print("please input a non-negative number")
            continue

        # def factorials(orgianl number):
        def factorials(user_num):
            # while counter < orginal number
            result = 1
            for i in range(1, user_num + 1):
                result *= i
            return result

        # disaply(f"{usernum}factored:{factorials(usernum)}"")
        print(f"{user_num} factored: {factorials(user_num)}")

        # actions = false didnt have the retry function 
        again = input("Do you want to compute another factorial?: ").strip().lower()
        #making sure they want to go again
        if again != "yes":
            action = False

    # exept value error:
    except ValueError:
        # disaply("please input a number") contuine
        print("input a number")
        # disaply("please input a number") contuine
        input("please input a number")