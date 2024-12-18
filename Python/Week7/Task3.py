# 3. Bird has features name and amount of eggs.  
# Amount of eggs has to be between 1 and 10.
# Migratory has special features: 
# there is attribute named country 
# that is the destination country and month 
# when the migration mainly occurs.
# Country name has to begin with a cap and 
# its length has to be between 5 to 20.
# Month has to be between 1 and 12.

class Bird:
    def __init__(self,name, eggs):
        self.name = name
        self.eggs = eggs
    
    def setName(self,name):
        self.name = name

    def setEggs(self,eggs):
        if eggs > 10 or eggs < 1:
            print("Amount of eggs has to be between 1 and 10")
        else:
            self.eggs = eggs

    def getBird(self):
        return "Name of the bird is: " + self.name + " and amount of eggs are: " + str(self.eggs)

class Migratory(Bird):
    def __init__(self,country,month):
        self.country = country
        self.month = month
    
    def setCountry(self,country):
        countryCap = country.capitalize()
        if country != countryCap:
            print("Country name has to begin with a cap")
        elif len(country) < 5 or len(country) > 20:
            print("Country name length has to be between 5 to 20")
        else: 
            self.country = country

    def setMonth(self, month):
        if month < 1 or month > 12:
            print("Month has to be between 1 and 12") 
        else:
            self.month = month

    def getMigratory(self):
        return "Destination country is: " + self.country + " and the month of migratory is: " + str(self.month) 

#Test 1 
bird1 = Migratory("Spain",9)
print(bird1.getMigratory())
bird1.setName("Sparrow")
bird1.setEggs(5)
bird1.setCountry("Italy")
bird1.setMonth(8)
print(bird1.getBird())
print(bird1.getMigratory())
#Test 2 
bird1.setCountry("spain")
bird1.setCountry("Fiji")
bird1.setName("Common crane")
bird1.setEggs(100)
bird1.setMonth(13)