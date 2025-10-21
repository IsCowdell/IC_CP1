#IC 1st functions notes
# always set variables first
#define all functions
Health = 100 
monster_Health = 100

def damage(amount):
    if turn == "player":
     return Health - amount
    else:
        return monster_Health, Health, - amount 
monster_Health,player_health = damage(10,Health)
def add(x,y):

    return x+y


def initials(name):
    names = name.split("")
    initials = ""
    for name in names:
        initials += name[0]
    return initials


total = add(5,5)
print(total)

print(f"10+72 = {add(10,7)}")
x = 0 
while x < add(3,9):
    print("duck")
    x += 1
print("goose")

add(10,72)
print(f"a = {ord("a")}")
print(f"98 = {ord(98)}")
print(initials("Tia Larose"))