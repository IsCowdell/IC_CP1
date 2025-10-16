#IC 1st strength password 
#assigning the score a value 
score = 0
#making sure that length will be changed
length = False
#making sure that lower will be changed
lower = False
#making sure that upper will be changed
upper = False
#making sure that digit will be changed
digit = False
#making sure that unique will be changed
unique = False
#ask user what they want the password to be 
password = input("What is your Password?: ")
#make sure password is requied length
if len(password) >= 8:
     #once equal true don't check again
     length = True
     #for whatever password is and check mutple times
for X in password:
     #checking for lowercase
     if X.islower():
          lower = True
    #checking for uppercase 
     if X.isupper():
          upper = True
        #checking for numbers
     if X.isdigit:
          digit = True
        # checking for special characters
     if not X.isalnum():
          unique = True
#meets required length give point 
if length:
     score += 1
     #show user how they got point 
     print("You got a point for a long password")
     # if user has a lowcase give point 
if lower:
     score += 1
     #show user they got point 
     print("You got a point for having lowercase")
     #if user has an uppercase give point 
if upper:
     #show user they got point and add point 
     score += 1
     print("You got a point for having uppercase")
     #if user has special characters 
if digit:
     # add one to points and show user they got point for having digit 
     score += 1
     print("You got a point for having a digit")

if unique:
     # add one to points and show user they got point for having special characters 
     score += 1
     print("You got a point for having unique characters")
#setting the score requirments 
#if the score is less than two show user you have weak password
if score < 2:
     print("You have a weak password")
#if score equal to 3 show user you have moderate password
elif score == 3:
     print("You have a moderate password")
#if score equal 4 then show user you have a strong password 
elif score == 4:
     print("you have a strong password")
#if score equal 5 then show user you have a very strong password
elif score == 5:
     print("You have a very strong password")