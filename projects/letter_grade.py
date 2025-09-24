# IC, 1st Letter Grade

percentage_grade = int(input("What percentange do you have in biology?  "))

if percentage_grade >= 94 and percentage_grade <= 100:
    print(f"You got An A ")
elif percentage_grade >= 90 and percentage_grade <= 93: 
    print(f"You got an A-")
elif percentage_grade >= 87 and percentage_grade <= 89:
    print(f"you got a B+")
elif percentage_grade >= 84 and percentage_grade <= 86:
    print(f"you got a B")
elif percentage_grade >= 80 and percentage_grade <= 83:
    print(f"you got a B-")
elif percentage_grade >= 77 and percentage_grade <= 79:
    print(f"you got a C+")
elif percentage_grade >= 75 and percentage_grade <= 76:
    print(f"you got a C")
elif percentage_grade >= 70 and percentage_grade <= 74:
    print(f"you got a C-")
elif percentage_grade >= 67 and percentage_grade <= 69:
    print(f"you got a D+")
elif percentage_grade >= 64 and percentage_grade <= 66:
    print(f"you got a D")
elif percentage_grade >= 60 and percentage_grade <= 63:
    print(f"you got a D-")
elif percentage_grade >= 0 and percentage_grade <= 59:
    print(f"you got a F")


else:
    print(f"Yay you got really good or you failed! ")