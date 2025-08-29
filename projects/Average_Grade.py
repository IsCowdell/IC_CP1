# IC, 1st Average Grade Project

math_grade = input("what is your grade in math ")
english_grade = input("what is your grade in english")
art_grade = input("what is your grade in art")
seminary_grade = input("what is your grade in seminary")
biology_grade = input("what is your grade in biology")
coding_grade = input("what is your grade in coding")
world_civ_grade = input("what is your grade in world civillzations")

print("Your average grade is: " + str(round((int(math_grade)+int(english_grade)+int(art_grade)+int(seminary_grade)+int(biology_grade)+int(coding_grade)+int(world_civ_grade))/7,2)))




