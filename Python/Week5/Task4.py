# 4. Fill 2 arrays with some values and calculate the sum array
import random
array1 = []
array2 = []

for i in range(5):
    array1.append(random.randint(1,20))
for i in range(3):
    array2.append(random.randint(1,10))

print("Sum of array 1:",sum(array1))
print("Sum of array 2:",sum(array2))
print("Sum of array 1 and 2:",sum(array1+array2))