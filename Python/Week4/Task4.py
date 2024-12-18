import random
# Program throws dice 100 times 
# and tells amounts of different values (1, 2, 3, 4, 5, and 6).
# Hints:
# from random import randint
# scaling example [0,10]
# value = randint(0, 10)

v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0

for i in range(100):
    v = random.randint(1,6)

    if v == 1:
        v1 += 1
    elif v == 2:
        v2 += 1
    elif v == 3:
        v3 += 1
    elif v == 4:
        v4 += 1
    elif v == 5:
        v5 += 1
    elif v == 6:
        v6 += 1

print("Amount of 1's:", v1)
print("Amount of 2's:", v2)
print("Amount of 3's:", v3)
print("Amount of 4's:", v4)
print("Amount of 5's:", v5)
print("Amount of 6's:", v6)