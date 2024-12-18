import math

# 1. Returns the average of 2 integers
def avgOf2(a,b):
    avg = (a + b) / 2
    return avg
# Test 1.
print(avgOf2(2,4))

# 2. Returns the average of 4 floating point values.
def avgOf4(a,b,c,d):
    avg = (a+b+c+d) / 4
    return '{:.2}'.format(avg)
# Test 2.
print(avgOf4(1.5,3.5,4.4,7.8))

# 3. Returns the sum of an array.
def sumOfArray(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
# Test 3.
print(sumOfArray([6,2,3,4,5]))

# 4. Returns the factorial.
def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
# Test 4.
print(factorial(5))

# 5. Returns the biggest of 3 integers.
def maxOf3Int(a,b,c):
    max = a
    if a < b and b > c:
        max = b
    elif a < c and c > b:
        max = c
    return max
# Test 5.
print(maxOf3Int(7,8,6))
    
# 6. Returns the BMI.
def bmi(mass, height):
    BMI = mass / height / height

    if BMI < 15:
        cat = "(Very severely underweight)"
    elif BMI >= 15 and BMI < 16:
        cat = "(Severely underweight)"
    elif BMI >= 16 and BMI < 18.5:
        cat = "(Underweight)"
    elif BMI >= 18.5 and BMI < 25:
        cat = "(Normal healthy weight)"
    elif BMI >= 25 and BMI < 30:
        cat = "(Overweight)"
    elif BMI >= 30 and BMI < 35:
        cat = "(Moderately obese)"
    elif BMI >= 35 and BMI < 40:
        cat = "(Severely obese)"
    else:
        cat = "(Very severely obese)"

    print ("BMI is: {:.1f}".format(BMI),(cat))
# Test 6.
bmi(70,1.67)

# 7. Function returns the biggest of 5 integers.
def maxOf5Int(a,b,c,d,e):
    array = [a,b,c,d,e]
    max = array[0]
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
    return max
# Test 7.
print(maxOf5Int(8,2,3,4,5))

# 8. Calculates amount of combinations (try to use also an own factorial function here).
def combinations(n,k):
    combinations = factorial(n) / (factorial(k) * factorial(n-k))
    return int(combinations)
# Test 8.
print(combinations(5,3))

# 9. Calculates the standard deviation.
def stdDeviation(array):
    avg = sum(array)/len(array)
    sum2 = 0
    for i in range(len(array)):
        x = (array[i]-avg)**2
        sum2 += x
    variance = sum2/len(array)
    stdDeviation = math.sqrt(variance)
    return stdDeviation
# Test 9.
print("Standard deviation is:",'{0:.2f}'.format(stdDeviation([2,4,4,4,5,5,7,9])))

# 10. Searches for a value from an array.
def findValue(x):
    find = "Not found"
    for i in range(len(list1)):
        if list1[i] == x:
            find = "Found in position: "+str(i)
            break
    print(find)
# Test 10.
list1 = [5,10,25,40]
findValue(10)
findValue(6)

# 11. Calculates the square root of value 2 (create your own function).
# 2 = x**2
def sqrtOf2():
    x = 0.0
    y = 2.0
    while True:
        y = x**2
        if y > 1.999 and y < 2.001:
            break
        x += 0.0001
    return '{:.3}'.format(x)
# Test 11.
print(sqrtOf2())

# 12. Calculates an approximation of Neper's value (e)
def neperValue(a):
    n = 1
    e = 0.0
    for i in range(1,a+1):
        n *= i
        e += i / n
    return e
# Test 12.
print(neperValue(16))

# 13. Calculates  approximations of sin(x) and cos(x)
def sinAndCos(x):
    sinX = x
    cosX = 1.0
    sinTemp = 0.0
    cosTemp = 0.0
    n = 1
    while True:
        fs = factorial((2*n+1))
        fc = factorial((2*n))
        cosX += (-1)**n*x**(2*n) / fc
        sinX += (-1)**n*x**(2*n+1) / fs
        if '{:.7}'.format(cosX) == '{:.7}'.format(cosTemp) and '{:.7}'.format(sinX) == '{:.7}'.format(sinTemp):
            break
        n += 1
        cosTemp = cosX
        sinTemp = sinX

    print("cos("+str(x)+"):",'{:.7}'.format(cosX))
    print("sin("+str(x)+"):",'{:.7}'.format(sinX))
# Test 13.
sinAndCos(1)

# B1 Create a function that sorts an array by using selection sort.
def selectionSort(array):
    
    for i in range(len(array)-1):
        min = array[len(array)-1]
        for j in range(i,len(array)):
            if min > array[j]:
                min = array[j]
        array.insert(i,array.pop(array.index(min)))
    return array

# Test B1.
array = [3,24,1,5,6,8,19,22,55,2]
print(selectionSort(array))

# B2 Create a function that multiplies two arrays.

def twoArrayMult(array1,array2):
    array3 = []
    for i in range(len(array1)):
        array3.append(array1[i] * array2[i])
    
    return array3


# Test B2.
array1 = [1,2,3,4,5]
array2 = [2,3,2,3,2]

print(twoArrayMult(array1,array2))