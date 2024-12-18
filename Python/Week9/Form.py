# Check 4 different fields of a feedback form before it can be submitted. 
# E.g user has to give age, telephone number, homepage url, email and/or 
# other information and those values are checked 
# (contents cannot be empty, either).


from tkinter import *

class Person():
    def __init__(self, name, age, telephone, email):
        self.name = name
        self.age = age
        self.telephone = telephone
        self.email = email

    def getInfo1(self):
        info = "Name: " + self.name + "\nAge: " + self.age + "\nTelephone: " + self.telephone + "\nEmail: " + self.email
        return info

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Form")
        self.master.geometry("500x300")
        self.master = master
        self.grid()
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # 4 labels (title)
        self.nameLbl = Label(self, text="Name:")
        self.ageLbl = Label(self, text="Age:")
        self.teleLbl = Label(self, text="Telephone:")
        self.emailLbl = Label(self, text="Email:")
        
        # 4 entrys
        self.nameE = Entry(self, width=30)
        self.nameE.focus()
        self.ageE = Entry(self, width=5)
        self.teleE = Entry(self, width=15)
        self.emailE = Entry(self, width=30)

        # 4 labels (errors)
        self.nameError = Label(self, text="")
        self.ageError = Label(self, text="")
        self.teleError = Label(self, text="")
        self.emailError = Label(self, text="")

        # buttons
        self.subBut = Button(self, text="Submit", width=10, command=self.submit)
        self.getBut = Button(self, text="Get info", width=10, command=self.getInfo)

        # Text
        self.info = Text(self, width=50, height=4)

        # Grid
        self.nameLbl.grid(row=0, column=0, sticky="e")
        self.nameE.grid(row=0, column=1, pady=1, sticky="w")
        self.nameError.grid(row=1, column=1, sticky="w")

        self.ageLbl.grid(row=2, column=0, sticky="e")
        self.ageE.grid(row=2, column=1, sticky="w")
        self.ageError.grid(row=3, column=1, sticky="w")

        self.teleLbl.grid(row=4, column=0, sticky="e")
        self.teleE.grid(row=4, column=1, sticky="w")
        self.teleError.grid(row=5, column=1, sticky="w")
        self.subBut.grid(row=5, column=2, sticky="w")

        self.emailLbl.grid(row=6, column=0, sticky="e")
        self.emailE.grid(row=6, column=1, sticky="w")
        self.getBut.grid(row=6, column=2, sticky="w")
        self.emailError.grid(row=7, column=1, sticky="w")
        

        self.info.grid(row=8, column=1, columnspan=2)

    def submit(self):
        name = str(self.nameE.get())
        age = str(self.ageE.get())
        telephone = str(self.teleE.get())
        email = str(self.emailE.get())

        if name == "":
            self.nameError.config(text="Enter name", bg="red2")
        else:
            self.nameError.config(text="", bg="SystemButtonFace")
        if age == "":
            self.ageError.config(text="Enter age", bg="red2")
        else:
            self.ageError.config(text="", bg="SystemButtonFace")
        if telephone == "":
            self.teleError.config(text="Enter telephone", bg="red2")
        else:
            self.teleError.config(text="", bg="SystemButtonFace")
        if email == "":
            self.emailError.config(text="Enter email", bg="red2")
        else:
            self.emailError.config(text="", bg="SystemButtonFace")
        if name and age and telephone and email != "": 
            global person1
            person1 = Person(name, age, telephone, email)
            self.nameE.delete(0,END)
            self.ageE.delete(0,END)
            self.teleE.delete(0,END)
            self.emailE.delete(0,END)



    def getInfo(self):
        self.info.delete("1.0","end")
        global person1
        infoText = person1.getInfo1()
        self.info.insert(INSERT, infoText)



    def create_menu(self):
        mainmenu = Menu(self)
        self.master.config(menu = mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = root.destroy)
    
        





root = Tk()
Application(root)
root.mainloop()