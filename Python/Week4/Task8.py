# Program calculates the factorial of n (given in a variable)

n = 5
sum = 1
i = 1

for i in range(1, n+1):
    sum *= i
print(n,"!"," = ",sum,sep="")