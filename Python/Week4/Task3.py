# Program calculates sum: 5, 10, 15, .. 100.
# Use: for and while

i = 5
sum = 0

# for

#for i in range(5,105,5):
#    sum = sum + i
#print(sum)

# while

while i <= 100:
    sum = sum + i
    i += 5
print(sum)