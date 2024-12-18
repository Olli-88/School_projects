#Our programs uses Ohm's law to calculate the resistance.
#User gives voltage and current.
#Ohm's law R=U/I

u = float(input("Give a voltage(V): "))
i = float(input("Give a current(A): "))
r = u/i
print (r)
print ("Resistance is:",r,"Ω")
