# IC 1st User Sign In

passwordfirst = 12345
firstusername = "isabella"

username = input("what is your username? ")
password = input("what is your password? ")
check = username == firstusername 

false_password = password != passwordfirst
false_username = username != firstusername

if username == firstusername:
    print(f"Your username is true!")
elif username == false_username: 
     print(f" stop faking identies")
if password == passwordfirst: 
    print(f"Your password is true") 
elif  password  == false_password: 
   print(f"Stop trying to get into people's accounts")
else: 
     print(f"wow its really you!") # type: ignore