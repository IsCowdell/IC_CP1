#IC 1st functions notes
# always set variables first
#define all functions

def add(x,y):
    return x+y

def initials(name):
    names = name.split("")
    initials = ""
    for name in names:
        initials += name[0]

total = add(5,5)
print(total)

print(f"10+72 = {add(10,7)}")
x = 0 
while x < add(3,9):
    print("duck")
    x += 1
print("goose")

add(10,72)