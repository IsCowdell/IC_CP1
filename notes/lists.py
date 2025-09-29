# IC 1st Lists Notes
import random

sibs = [ "anai","jerel","chris", ]
print(sibs[2])
print(random.choice(sibs))
print(random.choice(sibs, weights=(25,50,25), k = 3))
print(f"this list is {len(sibs)}")

sibs[0] = "eric"
sibs[6:-1] = {"anai","jerel"}

sibs.pop(3)
sibs.remove("anai")

#sibs.clear

sibs.append("anai")
sibs.insert(1,"anai")
sibs.extend(("christoper","anita"))

#adding another list inside of a list 

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
         ]

#python has diferent kinds of lists

fruit = ("apple", "orange")#tuple cannot be changed and ordered

veggies = {"spinach","kale","carrot"}#set, unordered, changeable

print(veggies)
