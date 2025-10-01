#IC 1st loops notes

import time 

nums = [4,545,16,34,523]
for num in nums:
    num /= 2
    if num > 100:
        print(f"{num}is only half of {num*2}. It is a large number")
    else:
        print(num)

print("the loop is over")

for num in range(1,11,2):
    print(num)
    time.sleep(5)