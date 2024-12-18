from tkinter import *
from string import ascii_uppercase

#Source - https://heritageguitars.com/pages/date-your-heritage

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Heritage serial number")
        self.master.geometry("300x100")
        self.master = master
        self.grid()
        self.create_widgets()
        self.create_menu()
        self.master.bind("<Return>", self.Heritage)

    def create_widgets(self):
        #Entry
        self.entry1 = Entry(self, width=30)
        #Button
        self.btn1 = Button(self, text="Search", command=self.Heritage)
        #Labels
        self.lbl1 = Label(self, text="Give your Heritage guitar serial number: ")
        self.lbl2 = Label(self)
        #Grids
        self.lbl1.grid(row=0,column=0, columnspan=2)
        self.entry1.grid(row=1, column=0)
        self.btn1.grid(row=1, column=1)
        self.lbl2.grid(row=2, column=0)


    def create_menu(self):
        mainmenu = Menu(self)
        self.master.config(menu = mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = root.destroy)

    def Heritage(self, event=None):
        alphabets = ascii_uppercase
        aL = list(alphabets)
        serialEntry = self.entry1.get()
        serial = serialEntry.upper()
        print(serial)
        first = serial[:1]
        firstTwo = serial[:2]
        try:
            if first == "1":
                year = "20"+ serial[1:3]
            if first == "A":
                for i in range(0,11):
                    if aL[i] == firstTwo[1:2]:
                        year = str(2010 + i)
            if firstTwo == "HC":
                year = "20" + serial[3:5]
            else:
                for i in range(1,len(aL)):
                    if aL[i] == first:
                        year = str(1985 + i - 1)
            self.lbl2["text"] = "Your guitar was built in: " + year
        except:
            self.lbl2["text"] = "Invadid serial number, try again!"

root = Tk()
Application(root)
root.mainloop()