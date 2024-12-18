#Student - Course (association class needed)

class Student:
    def __init__(self, firstname, surename, studentnro):
        self.firstname = firstname
        self.surename = surename
        self.studentnro = studentnro

    def getInfo(self):
        studentInfo = "Name: " + self.firstname + " " + self.surename + "\nStudent number: " + str(self.studentnro)
        return studentInfo

class Course:
    def __init__(self, name, courseCode):
        self.name = name
        self.courseCode = courseCode

    def getInfo(self):
        courseInfo = "Course: " + self.name + " (" + str(self.courseCode) + ")"
        return courseInfo

class Implementation:
    def __init__(self, student, course, startDate, endDate):
        self.student = student
        self.course = course
        self.startDate = startDate
        self.endDate = endDate

    def getInfo(self):
        info = self.student.getInfo()
        info += "\n" + self.course.getInfo()
        info += "\nTiming: " + self.startDate + " - " + self.endDate
        return info


stundet1 = Student("John","Doe",123456)
course1 = Course("Developing Python Applications", "AV00AE31/OJ/3002")
implementation1 = Implementation(stundet1,course1,"27.01.2021","14.04.2021")
print(implementation1.getInfo()) 