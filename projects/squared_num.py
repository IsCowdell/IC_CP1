#IC 1st squared Num
#Making A list with all the numbers
new_num = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

#Defining the function to mutply 
def mutply(new_num):
    return new_num ** 2
new_nums =map(lambda num :num**2,new_num)
              

for nums in new_nums:
    print(f"orginal numbernew number: {nums} ")
