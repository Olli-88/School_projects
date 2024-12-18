# 1. Array contains 30 random values. Calculate the sum and average.
# 2. Find the maximun of an array.
# 3. Search a value from an array.
import random

values = []
for i in range(30):
    values.append(random.randint(0,100))
max = values[0]
for i in range(len(values)):
    if values[i] > max:
        max = values[i]

print(values)
print("Sum is: ",sum(values))
print("Average is: ",(sum(values)/len(values)))
print("Max is: ",max)

find = int(input("Find value: "))
result = "Not found"
for i in range(len(values)):
    if values[i]== find:
        result = "Found in position",(i)
        break
print(result)