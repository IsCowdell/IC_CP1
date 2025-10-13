#IC 1st strength password

#Assign a score a value 
score = 0 
#Ask user for password and assign password a value and remove white spaces
password = input("What do you want your password to be? ").strip()
#assign your password a variable
X = password
#define length of password
length = len(password)
if length >= 8:
        #and then print you get another point and a good password
        print("wow you have a long password")
        #add another point
        score + 1
    #if not true then show the user you lost a point 
else:
     print("you missed this point")

#check if the password has lowercases 
for X in password:
    if X.islower() == True:
        #if it has lowercase prints you get one point 
        print("wow you have lowercases")
         #add score one point 
        score + 1
    
    #else show the user you missed a point and try again 

    if X.isupper() == True: 
        #print you get one point and has a pretty good score
        print("you have and uppercase good job + one point ")
        #add one point 
        score + 1 
        
     #else show the user you missed a point and try again 

      elif length >= 8:
  
  
      #else show the user you missed a point and try again 
    else:
        print()
        
    #else show the user you missed a point and try again 







#then check if the values are lowcases or uppercases 
#contuinely add one too the score if they get a uppercase or lowercase and a special character and number
#criteria is one uppercase, one lowercase, special character, and a number
# if the user has 1-2 points then show your user your password is very weak 3 points: Moderate 4 points: Strong 5 points: Very Strong







