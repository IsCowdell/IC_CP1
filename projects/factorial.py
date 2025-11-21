#IC 1st 
#and jacob 
#action = true
action = True
#while action:
while action:
#usernum is asked"what number do you want to set a factorial number for,? all decimals will be rouhoer"
    user_num = input("what number do you want to set a factoria number for,? all decmials will be rouhoer:  ")
    #actions = True : counter = 1
    action = True 
    counter = 1 
#try int(user_num): 
try:
 
 int(user_num)
    #actions = false
    actions = False
#exept value error:
except ValueError:
#disaply("please input a number") contuine
    print("input a number") 

#disaply("please input a number") contuine
# def factorials(orgianl number):
#while counter < orginal number
#minus = orginal nymber - counter
#og = og*minus : counter +=1 
#return og()

#disaply(f"{usernum}factored:{factorials(usernum)}"")
