# 6. Take a look at python.org site. 
# Array methods are presented here:
# https://docs.python.org/3/tutorial/datastructures.html
# Give your own examples of using those metods
 

list1 = [3,2,1]
list2 = [1,2,3,4,5,6,7,8]

list1.sort()
print(list1)

list1.append(4)
print(list1)

list2.extend(list1)
print(list2)

list1.insert(0,0)
print(list1)

list2.remove(8)
print(list2)

x = list2.pop()
print(list2)
print(x)

print(list2.count(3))

list2.clear()
print(list2)

print(list1.index(1))

list2 = list1.copy()
print(list2)

list2.reverse()
print(list1)
print(list2)