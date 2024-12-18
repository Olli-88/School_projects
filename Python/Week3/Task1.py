#User gives a value and our program tells if the value is > 100 or not.

i = float(input("Give value: "))

if i == 100:
    print ("Value is a hundred")
elif i < 100:
    print ("Value is under hundred")
else:
    print ("Value is over hundred")
