#Convert seconds to hours, minutes, seconds.
#3600s = 1h, 60s = 1min.

sec = int(input("Give seconds: "))

h = sec / 3600
m = (sec / 60) % 60
se = sec - int(h) * 3600 - int(m) * 60

print ("Hours:",int(h))
print ("Minutes:",int(m))
print ("Seconds:",int(se))
