from tkinter import *

class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Calculator")
        self.master.geometry("200x250")
        self.master = master
        self.grid()
        self.create_widgets()
        self.create_menu()
        self.master.bind("<Return>", self.enter)
        self.master.bind("<Escape>",self.cancel)
        

    def create_menu(self):
        mainmenu = Menu(self)
        self.master.config(menu = mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = root.destroy)

    def create_widgets(self):
        #Entry 
        self.e1 = Entry(self, font="Verdana,30")
        self.e1.grid(row=0, column=0, columnspan=4, padx=1, pady=3)
        self.e1.focus()
        #Buttons 
        self.bDivide = Button(self, text="/", height=2, width=4,command=self.divide).grid(row=1, column=1, padx=1, pady=1)
        self.bMulti = Button(self, text="*", height=2, width=4,command=self.multiply).grid(row=1, column=2, padx=1, pady=1)
        self.bMinus = Button(self, text="-", height=5, width=4,command=self.minus).grid(row=1, column=3, rowspan=2, padx=1, pady=1)
        self.bPlus = Button(self, text="+", height=5, width=4, command=self.plus).grid(row=3, column=3, rowspan=2, padx=1, pady=1)

        self.b1 = Button(self, text="1", height=2, width=4, command=lambda: self.numBut(1)).grid(row=4, column=0, padx=1, pady=1)
        self.b2 = Button(self, text="2", height=2, width=4, command=lambda: self.numBut(2)).grid(row=4, column=1, padx=1, pady=1)
        self.b3 = Button(self, text="3", height=2, width=4, command=lambda: self.numBut(3)).grid(row=4, column=2, padx=1, pady=1)

        self.b4 = Button(self, text="4", height=2, width=4, command=lambda: self.numBut(4)).grid(row=3, column=0, padx=1, pady=1)
        self.b5 = Button(self, text="5", height=2, width=4, command=lambda: self.numBut(5)).grid(row=3, column=1, padx=1, pady=1)
        self.b6 = Button(self, text="6", height=2, width=4, command=lambda: self.numBut(6)).grid(row=3, column=2, padx=1, pady=1)

        self.b7 = Button(self, text="7", height=2, width=4, command=lambda: self.numBut(7)).grid(row=2, column=0, padx=1, pady=1)
        self.b8 = Button(self, text="8", height=2, width=4, command=lambda: self.numBut(8)).grid(row=2, column=1, padx=1, pady=1)
        self.b9 = Button(self, text="9", height=2, width=4, command=lambda: self.numBut(9)).grid(row=2, column=2, padx=1, pady=1)

        self.b0 = Button(self, text="0", height=2, width=10, command=lambda: self.numBut(0)).grid(row=5, column=0, columnspan=2, padx=1, pady=1)
        
        self.bEnter = Button(self, text="Enter", height=2, width=10, command=self.enter).grid(row=5, column=2, columnspan=2, padx=1, pady=1)
        self.bCancel = Button(self, text="C", height=2, width=4, command=self.cancel).grid(row=1, column=0, padx=1, pady=1)

    
    def numBut(self,x):
        entrytext = self.e1.get()
        self.e1.delete(0,END)
        self.e1.insert(0,entrytext + str(x))

    def cancel(self, event=None):
        self.e1.delete(0,END)
        global sum1
        sum1 = 0
        latest = ""
        

    def plus(self,event=None):
        fNum = self.e1.get()
        self.e1.delete(0,END)
        global sum1
        sum1 += int(fNum)
        global latest
        latest = "plus"

    def minus(self,event=None):
        fNum = self.e1.get()
        self.e1.delete(0,END)
        global sum1
        if sum1 == 0:
            sum1 = int(fNum)
        else:
            sum1 -= int(fNum)
        global latest
        latest = "minus"

    def divide(self, event=None):
        fNum = self.e1.get()
        self.e1.delete(0,END)
        global sum1
        if sum1 == 0:
            sum1 = int(fNum)
        else:
            sum1 /= int(fNum)
        global latest
        latest = "divide"

    def multiply(self, event=None):
        fNum = self.e1.get()
        self.e1.delete(0,END)
        global sum1
        if sum1 == 0:
            sum1 = int(fNum)
        else:
            sum1 *= int(fNum)
        global latest
        latest = "multiply"

    def enter(self, event=None):
        sNum = self.e1.get()
        self.e1.delete(0,END)
        global sum1
        global latest
        if latest == "plus":
            self.e1.insert(0, sum1 + int(sNum))
        if latest == "minus":
            self.e1.insert(0, sum1 - int(sNum))
        if latest == "divide":
            self.e1.insert(0, sum1 / int(sNum))
        if latest == "multiply":
            self.e1.insert(0, sum1 * int(sNum))
        sum1 = 0
        


sum1 = 0

root = Tk()
Calculator(root)
root.mainloop()