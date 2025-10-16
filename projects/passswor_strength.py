#IC 1st strength password

#Assign a score a value 
score = 0 
#Ask user for password and assign password a value and remove white spaces
password = input("What do you want your password to be? ").strip()
#assign your password a variable
X = password
#define length of password
length = len(password)
#checking if length fits criteria 
if length >= 8:
        #and then print you get another point and a good password
        print("wow you have a long password")
        #add another point and show user score
        score += 1
        print(f"this is your score {score}")
    #if not true then show the user you lost a point 
else:
     print("you missed this point")

#check if the password has lowercases 

for X in password:
    if X.islower() != True:
        print("you lost a point")

    else:
       #if it has lowercase prints you get one point 
        print("wow you have lowercases")
         #add another point and show user score
        score += 1 
        print(f"this is your score {score}")
pass

for X in password:

    if X.isupper() == True: 
        #print you get one point and has a pretty good score
        print("you have and uppercase good job + one point ")
       #add another point and show user score
        score += 1 
        print(f"this is your score {score}")
        
      #else show the user you missed a point and try again 
    else:
        print("you lost a point")
       


  
    
for X in password:     
    #check if password has digit
    if any(X.isdigit()) != True:
    #else show the user you missed a point try again
        print("you lost point")
    else:
         #show the user that they have a number 
         print("You have a number lets goooo")
        #add another point and show user score
         score += 1 
         print(f"this is your score {score}")
         
    break
         
else:
     print("you need a new password ")
    






#then check if the values are lowcases or uppercases 
#contuinely add one too the score if they get a uppercase or lowercase and a special character and number
#criteria is one uppercase, one lowercase, special character, and a number
# if the user has 1-2 points then show your user your password is very weak 3 points: Moderate 4 points: Strong 5 points: Very Strong







