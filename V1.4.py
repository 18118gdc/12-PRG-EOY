from tkinter import *
from datetime import *
from tkinter import font
from tkinter.font import families

OrderType = str("")

def RetInfo():
    File = open("E:/PRG/12PRG/Python Coding/EOY/Menu.txt" ,"r")
    FileList1 = ((File.read()).split("\n")) 
    FileList2 = []
    for main in range(len(FileList1)):
        FileList2.append((FileList1[main]).split("/"))  
    return(FileList2)

def CustPage(PizzaData):
    global OrderType

    Win1 = Tk()
    Win1.geometry("1280x720")
    Win1.config(bg="#fff2cc")

    PickBut = Button(Win1,text=("Pick Up"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(PickFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    DeliBut = Button(Win1,text=("Delivery"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    NameBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    AddrBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    PhonBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    ContBut = Button(Win1,text="Continue",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(ContFun(PizzaData,NameBox.get(),AddrBox.get(),PhonBox.get())))
    ExitBut = Button(Win1,text="Exit",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(ExitFun(Win1)))
    CleaBut = Button(Win1,text="Clear",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(CleaFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))

    PickBut.pack()
    DeliBut.pack()
    NameBox.pack()
    AddrBox.pack()
    PhonBox.pack()

    ContBut.pack()
    ExitBut.pack()
    CleaBut.pack()

    Win1.mainloop()
    return

def PickFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox):
    global OrderType
    OrderType = ("Pick Up")
    PickBut.config(state="disabled")
    DeliBut.config(state="normal")
    NameBox.config(state="normal")
    AddrBox.config(state="disabled")
    PhonBox.config(state="disabled")
    AddrBox.delete(0,"end")
    PhonBox.delete(0,"end")
    return

def DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox):
    global OrderType
    OrderType = ("Delivery")
    PickBut.config(state="normal")
    DeliBut.config(state="disabled")
    NameBox.config(state="normal")
    AddrBox.config(state="normal")
    PhonBox.config(state="normal")   
    return

def ContFun(PizzaData,Name,Address,Phone):
    if ((OrderType) == ("Pick Up")):
        if Name == "":
            print("Error in Name")
        else:
            MenuPage(PizzaData)
    elif ((OrderType) == ("Delivery")):
        if Name == "":
            print("Error in Name")
        elif Address == "":
            print("Error in Address")
        elif Phone =="":
            print("Error in Phone")
        else:
            MenuPage(PizzaData)
    else:
        print("Error in Order Type")
    return

def ExitFun(Win):
    Win.destroy()
    return

def CleaFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox):
    global OrderType
    OrderType = ("")
    PickBut.config(state="normal")
    DeliBut.config(state="normal")
    NameBox.delete(0,"end")
    AddrBox.delete(0,"end")
    PhonBox.delete(0,"end")
    NameBox.config(state="disabled")
    AddrBox.config(state="disabled")
    PhonBox.config(state="disabled")

    return

def MenuPage(PizzaData):
    Win2 = Toplevel()
    Win2.title("Tony's Pizza Menu")
    Win2.geometry("1060x720")
    Win2.config(bg="#fff2cc")

    TitleText = Label(Win2,text="Tony's Pizza")
    SubText1 = Label(Win2,text = "Standard Pizzas") 

    Pizza1Text = Label(Win2,text = (PizzaData[0][0]),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))
    Pizza2Text = Label(Win2,text = (PizzaData[1][0]),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))

    Pizza1But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10 italic"),command=lambda:PopOutFun(PizzaData,1))

    ExitBut = Button(Win2,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),command=lambda:(ExitFun(Win2)))
    OrderBack = Label(Win2,text=(""),bg=("#cfe2f3"))
    OrderText = Label(Win2,text=("Order"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    TitleText.pack()
    SubText1.pack()

    Pizza1Text.pack()
    Pizza2Text.pack()
    Pizza1But.pack()
    ExitBut.pack()
    OrderBack.place(x=40,y=40,height="320",width="320")
    return

def PopOutFun(PizzaData,PizzaNum):
    
    if (PizzaData[PizzaNum][1] == "8.5"):
        PizzaType = str("Standard "+"$8.50")
    elif (PizzaData[PizzaNum][1]) == "13.5":
        PizzaType =str("Gorumet "+"$13.50")

    Win3 = Toplevel()
    Win3.geometry("1060x720")
    Win3.config(bg="#fff2cc")

    TitleText = Label(Win3,text=("Tony's Pizza"),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))
    SubText1 = Label(Win3,text=(PizzaData[PizzaNum][0]),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic")) 
    PizzaText = Label(Win3,text=(PizzaType),font=("{Trebuchet MS} 10 italic"))
    PizzaInfoText = Label(Win3,text=(PizzaData[PizzaNum][2]))

    PizzaText.pack()
    PizzaInfoText.pack()

    return

PizzaData = RetInfo()
CustPage(PizzaData)
