#IC 1st Basic Calculator 

number1 = float(input("what is your favorite number: "))
number2 = float(input("what is your least favorite number: "))

div = round(number1/number2,2)
subtraction = round(number1 - number2,2)
add = round(number1 + number2,2)
multi = round(number1 * number2,2)
floor_div = round(number1//number2,2)
mod = round(number1%number2,2)
exponets = round(number1**number2,2)

print(f"{number1} + {number2} = {add}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multi}")
print(f"{number1} / {number2} = {div}")
print(f"{number1} // {number2} = {floor_div}")
print(f"{number1} % {number2} = {mod}")
print((f"{number1} ** {number2} = {exponets}"))