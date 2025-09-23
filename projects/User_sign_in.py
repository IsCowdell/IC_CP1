# IC 1st User Sign In

correct_username = "isabella"
correct_password = 12345

username = input("What is your username? ")
password = input("What is your password? ")



if username == correct_username:
    print("Your username is correct!")
else:
    print("Stop faking identities!")


if password == correct_password:
    print("Your password is correct!")
else:
    print("Stop trying to get into people's accounts!")


if username == correct_username and password == correct_password:
    print("Wow, it's really you!")
