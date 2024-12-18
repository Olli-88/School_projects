#Create a euro converter: dollars to euros.
#Rate from Google (28.1.2021): 1 EUR = 1,21 USD

usd = float(input("Give amount(USD): "))
rate = 1.21
eur = usd / rate

print ("{:.2f}".format(usd),"USD is","{:.2f}".format(eur),"EUR")
