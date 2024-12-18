#Convert euros to 5, 10, 20, 50, 100, 200, 500 euros bills.

eur = int(input("Give amount(€): "))

fh = eur / 500
th = (eur - (int(fh)*500)) / 200
h = (eur - (int(fh)*500+int(th)*200)) / 100
ft = (eur - (int(fh)*500+int(th)*200+int(h)*100)) / 50
tw = (eur - (int(fh)*500+int(th)*200+int(h)*100+int(ft)*50)) / 20
t = (eur - (int(fh)*500+int(th)*200+int(h)*100+int(ft)*50+int(tw)*20)) / 10
f = (eur - (int(fh)*500+int(th)*200+int(h)*100+int(ft)*50+int(tw)*20+int(t)*10)) / 5
c  = eur % 5

print ("500€ bills:",int(fh))
print ("200€ bills:",int(th))
print ("100€ bills:",int(h))
print ("50€ bills:",int(ft))
print ("20€ bills:",int(tw))
print ("10€ bills:",int(t))
print ("5€ bills:",int(f))
print ("Coins:",(c))
