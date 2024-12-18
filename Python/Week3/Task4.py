#User gives a month number and our program tells
#the number of days in that month.
# 28 = 2
# 30 = 4,6,9,11
# 31 = 1,3,5,7,8,10,12

m = int(input("Give number of a month (1-12): "))

if m == 2:
    print("There are 28 days on this month (29 if it is a leap year)")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("There are 30 days on this month")
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("There are 31 days on this month")
