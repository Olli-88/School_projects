import math
import string
import hashlib

# Examples of string.ascii_uppercase and string.capwords()
# from string-module

# With string.capwords() you can clean fast string that has names.
# First words are split by given separator. After that every word
# is capitalized and they are joint back together. if separator is None
# or empty, whitespaces are replaced with single space, and all whitespaces
# in front and end of the string are removed#
x = "   denmark  finland   sweden       norway      iceland      "
y = string.capwords(x, sep= None)
print(y)

# With string.ascii_uppercase you can easily get all alphabets 
# for your projects. I've been using this while practising writing
# in excel with python. You don't have to write every alphabet by yourself
# you can just use for loop#
ALPHABETS = string.ascii_uppercase
AL = list(ALPHABETS)
print(AL)

# Here is part of my practising with excel and python.
# (Excel handling is by openpyxl) 
#
# wb = load_workbook("first.xlsx")
# sheet1 = wb.active
# ALPHABETS = ascii_uppercase
# AL = list(ALPHABETS)

# for i in range(len(AL)):
#     sheet1.cell(row=(i+2), column=1).value = AL[i]
#     sheet1.cell(row=1, column=(i+2)).value = i+1

# wb.save("first.xlsx")




# Examples of math.ceil and math.factorial from math-module
# 
# With math.ceil you can round up your floatnumber 
# to next up integer.
# This is useful, example if you need to calculate 
# how many full units you need.

# Amount of wine in class
wineclass = 0.2
# Full bottle
bottle = 0.7
# Guests
guests = 20

# How many bottles is needed
bottles = guests * wineclass / bottle
# How many full bottles is needed
full_bottles = math.ceil(bottles)

print("You need:", full_bottles, "full bottles.")



# There is a built in function for factorial in math-module. 
print("math.factorial(5) is:",math.factorial(5))

# For example here is my version for calculatin factorial from week6 tasks.
# It is easier to use that math.factorial function, but with making
# your own function, it is easier to understand how they actually work.

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
print("My own factorial function for n=5:",factorial(5))



# Examples of haslib.sha512 and hashlib.hexdigest from haslib-module

# Normally password shouldn't be stored in plain text,
# but for this example it is more easyer to explain
# how this module works 

# hashlib.sha512() converts bytes-like object into SHA-512. 
# In this example password is cryptred that it is almost impossiple to
# decipher without knowing the original password.
# Hash function are basicly one-way funciton.
password = str.encode("Cat1")
hashed_password = hashlib.sha512(password).hexdigest()
print(hashed_password)

# With hashlib.hexdigest() we can make sha512 more readable and in
# this example we can compare digested values of original password
# and given password.
x = str.encode(input("Password: "))
hashed_password2 = hashlib.sha512(x).hexdigest()

if hashed_password == hashed_password2:
    print("Welcome!")
else:
    print("Wrong password!")
