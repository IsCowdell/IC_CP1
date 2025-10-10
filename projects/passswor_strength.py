#IC 1st strength password
#first assign value for score and after that assign value for letters and then check if all the letters are lowcase and then ask user for their passwd after make sure that the password doesn't have any white spaces
#then check if the values are lowcases or uppercases 
#contuinely add one too the score if they get a uppercase or lowercase and a special character and number 
#quit 

score = 0 
#assign score a value 
password = input("give me a password")
#ask the user for password
password.strip
#making sure that the user won't break the code
for x in password: 
    while password <= len(8):
    #checking if password is long enough 
    print("your password is long enough")
    score += 1
if password == x.lower():


