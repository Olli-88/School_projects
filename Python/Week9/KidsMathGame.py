# kids math game (add prize: pic, sound or something else (negative/positive)) 
# Two numbers are shown on labels
# User adds the sum to a textbox
# With a button sum is checked
# Then new values are generated to labels
# Right and wrong answers are shown
import random
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Kids math game")
        self.master.geometry("300x200")
        self.master = master
        self.grid()
        self.create_widgets()
        self.create_menu()
        self.responsive()
        self.master.bind("<Return>", self.onSubmit)

        

    def responsive(self):
        for i in range(4):
            root.columnconfigure(i,weight=1)
            root.rowconfigure(i,weight=1)

    def create_widgets(self):
        #Labels 
        self.pic1 = PhotoImage(file="KidsMathGamePic1.png")
        self.pic2 = PhotoImage(file="KidsMathGamePic2.png")
        self.l1 = Label(self, text = "How much is " + str(val1) + " + " + str(val2))
        self.l2 = Label(self, text = "")
        self.l3 = Label(self, text = "")
        self.l4 = Label(self, text = "")
        self.l5 = Label(self, image=self.pic1)
        self.l1.grid(row=0, column=0, padx=2, pady=2, columnspan=2, sticky="w")
        self.l2.grid(row=3, column=0, padx=2, pady=1, columnspan=2, sticky="w")
        self.l3.grid(row=4, column=0, padx=2, pady=1, columnspan=2, sticky="w")
        self.l4.grid(row=5, column=0, padx=2, pady=1, columnspan=2, sticky="w")
        self.l5.grid(row=0, column=3, padx=2, pady=1, rowspan=5, sticky="e")
        
        #Entry (1)
        self.e1 = Entry(self, width=5, justify="center")
        self.e1.grid(row=1, column=0, padx=2, pady=2, sticky="w")
        self.e1.focus()

        #Button (1)
        self.b1 = Button(self, text="Submit", command=self.onSubmit)
        self.b1.grid(row=1, column=1, padx=2, pady=2)
    
    def onSubmit(self, event=None):
        global val1,val2
        sum1 = val1 + val2
        self.l2["text"] = "Your answer was: " + self.e1.get()
        self.l3["text"] = "Correct aswer was: " + str(sum1)
        val1 = random.randint(1,10)
        val2 = random.randint(1,10)
        self.l1["text"] = "How much is: " + str(val1) + " + " + str(val2)
        try:
            if sum1 == int(self.e1.get()):
                self.l4["text"] = "Your aswer was right!"
                self.l4.config(bg="green2")
                self.l5.config(image=self.pic1)
        
            else:
                self.l4["text"] = "Your aswer was wrong."
                self.l4.config(bg="red")
                self.l5.config(image=self.pic2)
        except:
                self.l4["text"] = "Your aswer was wrong."
                self.l4.config(bg="red")
                self.l5.config(image=self.pic2)
        self.e1.delete(0,"end")

    def create_menu(self):
        mainmenu = Menu(self)
        self.master.config(menu = mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = root.destroy)


val1 = random.randint(1,10)
val2 = random.randint(1,10)

root = Tk()
Application(root)
root.mainloop()