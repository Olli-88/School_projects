# There are 20 values in an array:
# calculate the standard deviation
import random
import math

array = []
for i in range(20):
    array.append(random.randint(1,10))
print(array)

avg = sum(array)/len(array)

sum2 = 0
for i in range(len(array)):
    x = (array[i]-avg)**2
    sum2 += x

variance = sum2/len(array)

stdDeviation = math.sqrt(variance)
print("Standard deviation is:",'{0:.2f}'.format(stdDeviation))