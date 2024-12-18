#User gives the lengths of the triangle's sides.
#Program tells what is the triangle like
#(e.g. is it right angled, isosceles...)
a = float(input("Give a length of the first side: "))
b = float(input("Give a length of the second side: "))
c = float(input("Give a length of the third side: "))
# if a == b and b == c and c == a:
if a == b == c:
    print("This is a acute-angled equilateral triangle")
elif a == b or b == c or c == a:
    print("This is a isosceles triangle")
else:
    print("This is a scalene triangle")
