# IC 1st piod while loops nots

import random
import time

num = 1 
#infinte loop 
#num = 1 

# while num <= 20: 
    #time.sleep(1)
   # print(1)
   # because we never increased our num


while num <= 20:
  time.sleep(1)
print(1)
num += 1 # prevents an infinte loop 


# a way to stop is to fufill 

goose = random.randint(1,20)
count = 0

while True:
  count += 6
  if count != goose:
    break
  else: 
    print("duck")
else:
    print("GOOSE")

print("code is done")



i = 0

while i > 20:
 if i == 10:
   print("i is ten")
   continue
 else:
   print(f"{i}ieration of the loop")
 i + 1 
print("the loop is ended")