#House with 3 Rooms (note:  composition)

class House:
    def __init__(self, name, address, rooms):
        self.name = name
        self.address = address
        self.rooms = rooms

    def getInfo(self):
        houseInfo = "House: " + self.name + "\nAddress: " + self.address
        for i in range(3):
            houseInfo += "\nRoom " + str(i+1) + ": " + rooms[i].getInfo()
        return houseInfo



class Room:
    def __init__(self, name, squareMetre):
        self.name = name
        self.squareMetre = squareMetre

    def getInfo(self):
        roomInfo = self.name + ", " + str(self.squareMetre) + "m^2"
        return roomInfo
        

        
room1 = Room("Bedroom", 20)
room2 = Room("Kitchen", 10)
room3 = Room("Living room", 20)

rooms = [room1, room2, room3]

house1 = House("House1","Street1", rooms)
print(house1.getInfo())