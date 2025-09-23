#☑️Elif and Logical Operators Notes IC 1st 

grade = 100
if grade > 100:
    print(f"you did extra credit...... you got {grade-100} extra credit! ")
elif grade == 100:
    print(f"YOU ARE PERFECT")
else:
    print(f"you suck try harder ")

username = "mslarose"
password = "37843"

user = input("enter your username: ")
word = input("enter your password: ")

if user == username and word == password:
    print("Welcome Ms.Larose")
elif user == username:
    pass
    print("password incorrect")
else: print("incorrect credtainls")