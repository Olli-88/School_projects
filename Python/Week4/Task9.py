# Program calculates the exponential value 
# (base and exponent are given invariable). 
# Base can be a real number, exponent is a whole number. 
# Use a loop.

base = 5
exponent = 5
sum = base

for i in range(exponent-1):
    sum *= base
print(base,"^",exponent," = ",sum,sep="")