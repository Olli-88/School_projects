# 2 arrays contain students grades in math and in English language.
# There are 10 students. Try to calculate the correlation.
import math
import random

arrayMath = []
arrayEng = []

for i in range(1,11):
    arrayMath.append(["Student "+str(i), random.randint(0,5)])
    arrayEng.append(["Student "+str(i), random.randint(0,5)])
#print(arrayMath)
#print(arrayEng)

sumMath = 0
sumEng = 0

for i in range(len(arrayMath)):
    sumMath += arrayMath[i][1]
    sumEng += arrayEng[i][1]

avg1 = sumMath/len(arrayMath)
avg2 = sumEng/len(arrayEng)
xy = 0
sumX = 0
sumY = 0
for i in range(len(arrayMath)):
    x = arrayMath[i][1]-avg1
    x2 = x**2
    y = arrayEng[i][1]-avg2
    y2 = y**2
    xy += x*y
    sumX += x2
    sumY += y2

covariance = xy/(len(arrayMath))
varianceX = sumX/len(arrayMath)
varianceY = sumY/len(arrayEng)
stdDevX = math.sqrt(varianceX)
stdDevY = math.sqrt(varianceY)
#print('{0:.2f}'.format(covariance))
#print('{0:.2f}'.format(stdDevX))
#print('{0:.2f}'.format(stdDevY))

correlation = covariance / (stdDevX * stdDevY) 

strenght = ""
text = "positive"

if correlation < 0:
    text = "negative"
    correlation *= -1

if correlation >= 0 and correlation < 0.3:
    strenght = "None or very weak"
elif correlation >= 0.3 and correlation < 0.5:
    strenght = "Weak"
elif correlation >= 0.5 and correlation < 0.7:
    strenght = "Moderate"
elif correlation >= 0.7 and correlation <= 1:
    strenght = "Strong"

if text == "negative":
    correlation *= -1


print("Correlation coefficien is: "'{0:.2f}'.format(correlation),"("+strenght,text,"correlation)")
