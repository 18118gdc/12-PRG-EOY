from tkinter import *
from datetime import *
from tkinter import font
from tkinter.font import families

def RetInfo():
    File = open("C:/Users/whcma/Documents/Coding/School/PRG/12PRG/Python Coding/EOY/Menu.txt" ,"r")
    FileList1 = ((File.read()).split("\n")) 
    FileList2 = []
    for main in range(len(FileList1)):
        FileList2.append((FileList1[main]). split(","))  
    return(FileList2)

def CustPage(PizzaData):
    Win1 = Tk()
    Win1.geometry("1280x720")
    Win1.config(bg="#fff2cc")

    PickBut = Button(Win1,text=("Pick Up"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(PickFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    DeliBut = Button(Win1,text=("Delivery"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    NameBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    AddrBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    PhonBox = Entry(Win1,text="",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    ContBut = Button(Win1,text="Continue",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10 italic"),command=lambda:(ContFun(PizzaData)))
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
    PickBut.config(state="disabled")
    DeliBut.config(state="normal")
    NameBox.config(state="normal")
    AddrBox.config(state="disabled")
    PhonBox.config(state="disabled")
    AddrBox.delete(0,"end")
    PhonBox.delete(0,"end")
    return

def DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox):
    PickBut.config(state="normal")
    DeliBut.config(state="disabled")
    NameBox.config(state="normal")
    AddrBox.config(state="normal")
    PhonBox.config(state="normal")   
    return

def ContFun():
    
    return

def ExitFun(Win1):
    Win1.destroy()
    return

def CleaFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox):
    PickBut.config(state="normal")
    DeliBut.config(state="normal")
    NameBox.delete(0,"end")
    AddrBox.delete(0,"end")
    PhonBox.delete(0,"end")
    NameBox.config(state="disabled")
    AddrBox.config(state="disabled")
    PhonBox.config(state="disabled")

    return

PizzaData = RetInfo()
CustPage(PizzaData)