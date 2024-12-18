#User gives the speed of the car (km/h) and the distance (km).
#Program calculates amount of time.
#a) in hours
#b) in whole hours and minutes

speed = float(input("Give the speed of the car (km/h): "))
dist = float(input("Give the distance (km): "))
time = dist / speed

print ("Answer a: It takes",(time),"hours to travel the distance")

h = int(time)
min = int((time - h) * 60)

if h == 0:
    print ("Answer b: It takes",(min),"minutes to travel the distance")
elif min == 0:
    print ("Answer b: It takes",(h),"hours to travel the distance")
else:
    print ("Answer b: It takes",(h),"hours and",(min),"minutes to travel the distance")

