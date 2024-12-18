#Group has 3 members (note: aggregation)

class Member:
    def __init__(self, firstname, surename):
        self.firstname = firstname
        self.surename = surename
    
    def getInfo(self):
        memberInfo = self.firstname + " " + self.surename
        return memberInfo

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def addMembers(self, m1, m2, m3):
        self.members.append(m1)
        self.members.append(m2)
        self.members.append(m3)
    
    def getInfo(self):
        info = "Group name is: " + self.name
        info += "\nMembers are:"
        for i in range(3):
            info += "\nMember"+ str(i+1) + ": " + self.members[i].getInfo()
        return info

member1 = Member("John", "Doe")
member2 = Member("Jane", "Doe")
member3 = Member("Charlie", "Brown")

group1 = Group("First group")
group1.addMembers(member1,member2,member3)
print(group1.getInfo())