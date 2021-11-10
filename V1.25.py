
from tkinter import *
from datetime import *
from tkinter import font
from tkinter.font import families

OrderType = str("")
PizzaOrder = [[]for main in range(2)]

def RetInfo():
    File = open("E:/PRG/12PRG/Python Coding/EOY/Menu.txt" ,"r")
    FileList1 = ((File.read()).split("\n")) 
    FileList2 = []
    for main in range(len(FileList1)):
        FileList2.append((FileList1[main]).split("/"))  
    return(FileList2)

def CustPage(PizzaData):
    global OrderType
    global Win1
    try:
        Win1.destroy()
    except:
        ()
    Win1 = Tk()
    Win1.geometry("594x192")
    Win1.config(bg="#fff2cc")
    Win1.title("Tony's Pizza Order Select")

    SubTitle1 = Label(Win1,text="Tony's Pizza",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 20"))
    PickBut = Button(Win1,text=("Pick Up"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(PickFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    DeliBut = Button(Win1,text=("Delivery"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    ErrorText = Label(Win1,text="",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    NameText = Label(Win1,text="Name:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    NameBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    PhonText = Label(Win1,text="Phone No.:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    PhonBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    AddrText = Label(Win1,text="Address:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    AddrBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    ContBut = Button(Win1,text="Continue",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(ContFun(PizzaData,NameBox.get(),AddrBox.get(),PhonBox.get(),OrderType,ErrorText)))
    ExitBut = Button(Win1,text="Exit",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(ExitFun()))
    CleaBut = Button(Win1,text="Clear",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(CleaFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    SubTitle1.place(x=30,y=10)
    PickBut.place(x=30,y=50,height=30,width=245)
    DeliBut.place(x=319,y=50,height=30,width=245)
    NameText.place(x=30,y=80)
    NameBox.place(x=30,y=100,height=22,width=144)
    PhonText.place(x=220,y=80)
    PhonBox.place(x=220,y=100,height=22,width=144)
    AddrText.place(x=420,y=80)
    AddrBox.place(x=420,y=100,height=22,width=144)
    ErrorText.place(x=30,y=120)
    ContBut.place(x=30,y=142,height=30,width=144)
    ExitBut.place(x=220,y=142,height=30,width=144)
    CleaBut.place(x=420,y=142,height=30,width=144)

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

def ContFun(PizzaData,Name,Address,Phone,OrderType,ErrorText):
    if ((OrderType) == ("Pick Up")):
        if Name == "":
            ErrorText.config(text="Error in Name")
        else:
            ErrorText.config(text="")
            MenuPage(PizzaData,OrderType,Name,Address,Phone)
    elif ((OrderType) == ("Delivery")):
        if Name == "":
            ErrorText.config(text="Error in Name")
        elif Phone == "":
            ErrorText.config(text="Error in Phone")
        elif Address =="":
            ErrorText.config(text="Error in Address")
        else:
            ErrorText.config(text="")
            MenuPage(PizzaData,OrderType,Name,Address,Phone)
    else:
        ErrorText.config(text="Error in Order Type")
    return

def ExitFun():
    global Win1
    Win1.destroy()
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

def MenuPage(PizzaData,OrderType,Name,Address,Phone):
    global PizzaOrder
    global Win2
    Win2 = Toplevel()
    Win2.title("Tony's Pizza Menu")
    Win2.geometry("960x460")
    Win2.config(bg=("#fff2cc"))

    OrderBack = Label(Win2,text=(""),bg=("#cfe2f3"))
    SubText1 = Label(Win2,text=("Tony's Pizza"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 24"))
    SubText2 = Label(Win2,text = ("Standard Pizzas"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 14")) 
    SubText3 = Label(Win2,text=("Gourmet Pizzas"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 14"))

    ErrorText2 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))

    Pizza1Text = Label(Win2,text = (PizzaData[0][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza2Text = Label(Win2,text = (PizzaData[1][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza3Text = Label(Win2,text = (PizzaData[2][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza4Text = Label(Win2,text = (PizzaData[3][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza5Text = Label(Win2,text = (PizzaData[4][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza6Text = Label(Win2,text = (PizzaData[5][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza7Text = Label(Win2,text = (PizzaData[6][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza8Text = Label(Win2,text = (PizzaData[7][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza9Text = Label(Win2,text = (PizzaData[8][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza10Text = Label(Win2,text = (PizzaData[9][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza11Text = Label(Win2,text = (PizzaData[10][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    Pizza12Text = Label(Win2,text = (PizzaData[11][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))

    OrderText = Label(Win2,text=("Order"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 30"))
    OrderText1 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText2 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText3 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText4 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText5 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderTextTot = Label(Win2,text=("TOTAL:"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost1 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost2 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost3 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost4 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost5 = Label(Win2,text=(""),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCostTot = Label(Win2,text=("${:,.2f}".format(float(CalcPizza(OrderType,PizzaOrder)))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    
    ExitBut = Button(Win2,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:(ExitFun()))

    OrderBut1 = Button(Win2,text=("X"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(0,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText2))
    OrderBut2 = Button(Win2,text=("X"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(1,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText2))
    OrderBut3 = Button(Win2,text=("X"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(2,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText2))
    OrderBut4 = Button(Win2,text=("X"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(3,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText2))
    OrderBut5 = Button(Win2,text=("X"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(4,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText2))
    
    Pizza1But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,0,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza2But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,1,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza3But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,2,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza4But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,3,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza5But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,4,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza6But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,5,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza7But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,6,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza8But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,7,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza9But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,8,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza10But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,9,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza11But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,10,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))
    Pizza12But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,11,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2))

    
    CanBut = Button(Win2,text=("Cancel"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RepFun())))
    CheckBut = Button(Win2,text=("Checkout"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:CheckFun(OrderType,PizzaOrder,Name,Address,Phone,ErrorText2)))
    

    SubText1.place(x=30,y=8)
    SubText2.place(x=30,y=50)

    Pizza1Text.place(x=30,y=75)
    Pizza1But.place(x=30,y=100,height=30,width=140)
    Pizza2Text.place(x=190,y=75)
    Pizza2But.place(x=190,y=100,height=30,width=140)
    Pizza3Text.place(x=350,y=75)
    Pizza3But.place(x=350,y=100,height=30,width=140)
    Pizza4Text.place(x=510,y=75)
    Pizza4But.place(x=510,y=100,height=30,width=140)
    Pizza5Text.place(x=30,y=135)
    Pizza5But.place(x=30,y=160,height=30,width=140)
    Pizza6Text.place(x=190,y=135)
    Pizza6But.place(x=190,y=160,height=30,width=140)
    Pizza7Text.place(x=350,y=135)
    Pizza7But.place(x=350,y=160,height=30,width=140)
    SubText3.place(x=30,y=200)
    Pizza8Text.place(x=30,y=225)
    Pizza8But.place(x=30,y=255,height=30,width=140)
    Pizza9Text.place(x=190,y=225)
    Pizza9But.place(x=190,y=255,height=30,width=140)
    Pizza10Text.place(x=350,y=225)
    Pizza10But.place(x=350,y=255,height=30,width=140)
    Pizza11Text.place(x=510,y=225)
    Pizza11But.place(x=510,y=255,height=30,width=140)
    Pizza12Text.place(x=30,y=285)
    Pizza12But.place(x=30,y=310,height =30,width=140)

    ExitBut.place(x=820,y=30,height=30,width=110)
    OrderBack.place(x=670,y=100,height=285,width=260)
    OrderText.place(x=750,y=105)    
    OrderTextTot.place(x=675,y=155)
    OrderCostTot.place(x=820,y=155)
    ErrorText2.place(x=820,y=390)
    CanBut.place(x=670,y=410,height=30,width=110)
    CheckBut.place(x=820,y=410,height=30,width=110)
    
    return

def SubFun(OrderPos,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderTextTot,OrderCostTot,ErrorText):
    if ((len(PizzaOrder[0]))<=0):
        ErrorText.config(text="Error No pizzas")
    elif ((len(PizzaOrder[0]))<=(OrderPos)):
        ErrorText.config(text="Error No Pizza in order slot")
    else:
        PizzaOrder[0].pop(OrderPos)
        PizzaOrder[1].pop(OrderPos)
        OrderTextTot.place_forget()
        OrderCostTot.place_forget()
        OrderCostTot.config(text=("${:,.2f}".format(float(CalcPizza(OrderType,PizzaOrder)))))
        try:
            OrderText1.config(text=(PizzaOrder[0][0]))
            OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
            try:
                OrderText2.config(text=(PizzaOrder[0][1]))
                OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][1]))))
                try:
                    OrderText3.config(text=(PizzaOrder[0][2]))
                    OrderCost3.config(text=("${:,.2f}".format(float(PizzaOrder[1][2]))))
                    try:    
                        OrderText4.config(text=(PizzaOrder[0][3]))
                        OrderCost4.config(text=("${:,.2f}".format(float(PizzaOrder[1][3]))))
                        OrderText5.config(text=(""))
                        OrderCost5.config(text=(""))
                        OrderBut5.place_forget()
                        OrderText5.place_forget()
                        OrderCost5.place_forget()
                        OrderTextTot.place(x=675,y=315)
                        OrderCostTot.place(x=820,y=315)
                    except:
                        OrderText4.config(text=(""))
                        OrderCost4.config(text=(""))
                        OrderBut4.place_forget()
                        OrderText4.place_forget()
                        OrderCost4.place_forget()  
                        OrderTextTot.place(x=675,y=275)
                        OrderCostTot.place(x=820,y=275)                      
                except:
                    OrderText3.config(text=(""))
                    OrderCost3.config(text=(""))
                    OrderBut3.place_forget()
                    OrderText3.place_forget()
                    OrderCost3.place_forget()
                    OrderTextTot.place(x=675,y=235)
                    OrderCostTot.place(x=820,y=235)
            except:
                OrderText2.config(text=(""))
                OrderCost2.config(text=(""))
                OrderBut2.place_forget()
                OrderText2.place_forget()
                OrderCost2.place_forget()
                OrderTextTot.place(x=675,y=195)
                OrderCostTot.place(x=820,y=195)
        except:
            OrderText1.config(text=(""))
            OrderCost1.config(text=(""))
            OrderBut1.place_forget()
            OrderText1.place_forget()
            OrderCost1.place_forget()
            OrderTextTot.place(x=675,y=155)
            OrderCostTot.place(x=820,y=155)
    return

def PopOutFun(PizzaData,PizzaNum,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2):
    try:
        global Win3
        Win3.destroy()
    except:
        ()
    CostReg = float(8.5)
    CostGor = int(5)
    if (float(PizzaData[PizzaNum][1]) == CostReg):
        PizzaType = str("Standard")
    elif (float(PizzaData[PizzaNum][1])) == (CostReg+CostGor):
        PizzaType =str("Gourmet")

    EntNum = int(0)
    PizzaDesc = (PizzaData[PizzaNum][2])
    for main in range(len(PizzaDesc)):
        if ((PizzaDesc[main:(main+1)]) == " "):
            EntNum+=1
            if ((EntNum)>=(2)):
                PizzaDesc = ((PizzaDesc[:main]) + "\n" + (PizzaDesc[(main+1):]))
                EntNum=0

    Win3 = Toplevel()
    Win3.geometry("369x220")
    Win3.config(bg="#fff2cc")
    Win3.title("Tony's Pizza Pizza Info.")

    PizzaBack = Label(Win3,text=(""),bg=("#6fa8dc"))
    TitleText = Label(Win3,text=("Tony's Pizza"),bg=("#fff2cc"),font=("{Trebuchet MS} 24"))
    SubText1 = Label(Win3,text=(PizzaData[PizzaNum][0]),bg=("#fff2cc"),font=("{Trebuchet MS} 14 italic")) 
    PizzaText1 = Label(Win3,text=(PizzaType),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10 italic"))
    PizzaText2 = Label(Win3,text=("${:,.2f}".format(float(PizzaData[PizzaNum][1]))),fg=("#ffffff"),bg=("#6fa8dc"),font=("{Trebuchet MS} 10 italic"))
    PizzaInfoText = Label(Win3,text=(PizzaDesc),anchor=W,bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))

    ErrorText3 = Label(Win3,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))

    AddBut = Button(Win3,text=("Add to Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:AddFun(len(PizzaOrder[0]),PizzaData,PizzaNum,AddBox.get(),OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2,ErrorText3))
    AddBox = Entry(Win3,bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    AddBox.insert(END,1)
    Exit = Button(Win3,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:ExitFun())
    RetBut = Button(Win3,text=("Return to Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RetFun(Win3))))

    TitleText.place(x=30,y=10)
    SubText1.place(x=27,y=60)
    PizzaBack.place(x=27,y=90,height=31,width=120)
    PizzaText1.place(x=30,y=93)
    PizzaText2.place(x=100,y=93)
    PizzaInfoText.place(x=30,y=122)
    ErrorText3.place(x=219,y=68)
    AddBox.place(x=220,y=90,height=31,width=20)
    AddBut.place(x=240,y=89,width=99)
    Exit.place(x=239,y=20,height=31,width=100)
    RetBut.place(x=219,y=126,width=120)
    return

def AddFun(PizzaOrderSize,PizzaData,PizzaNum,PizzaQt,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5,OrderCostTot,OrderType,OrderTextTot,ErrorText2,ErrorText3):
    global PizzaOrder
    try:
        PizzaQt=int(PizzaQt)
    except ValueError:
        ErrorText3.config(text="Error Invalid Qt.")
    if ((PizzaQt)<=0):
        ErrorText3.config(text="Error Invalid Qt.")
    elif ((PizzaOrderSize+PizzaQt)>=(6)):
        ErrorText3.config(text="Error 5 pizza max.")
    else:
        ErrorText2.config(text="")
        ErrorText3.config(text="")
        try:
            OrderTextTot.place_forget()
            OrderCostTot.place_forget()
            OrderText1.place_forget()
            OrderCost1.place_forget()
            OrderText2.place_forget()
            OrderCost2.place_forget()                
            OrderText3.place_forget()
            OrderCost3.place_forget()
            OrderText4.place_forget()
            OrderCost4.place_forget()
            OrderText5.place_forget()
            OrderCost5.place_forget()
        except:
            ()
        for main in range(PizzaQt):            
            PizzaOrder[0].append(PizzaData[PizzaNum][0])
            PizzaOrder[1].append(PizzaData[PizzaNum][1])
        OrderCostTot.config(text=("${:,.2f}".format(float(CalcPizza(OrderType,PizzaOrder)))))
        OrderText1.config(text=((PizzaOrder[0][0])))
        OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
        OrderBut1.place(x=870,y=157,height=20,width=27)
        OrderText1.place(x=675,y=155)
        OrderCost1.place(x=820,y=155)
        try:
            OrderText2.config(text=((PizzaOrder[0][1])))
            OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][1]))))
            OrderBut2.place(x=870,y=197,height=20,width=27)
            OrderText2.place(x=675,y=195)
            OrderCost2.place(x=820,y=195)
            try:
                OrderText3.config(text=((PizzaOrder[0][2])))
                OrderCost3.config(text=("${:,.2f}".format(float(PizzaOrder[1][2]))))
                OrderBut3.place(x=870,y=237 ,height=20,width=27)
                OrderText3.place(x=675,y=235)
                OrderCost3.place(x=820,y=235)
                try:
                    OrderText4.config(text=((PizzaOrder[0][3])))
                    OrderCost4.config(text=("${:,.2f}".format(float(PizzaOrder[1][3]))))
                    OrderBut4.place(x=870,y=277,height=20,width=27)
                    OrderText4.place(x=675,y=275)
                    OrderCost4.place(x=820,y=275)
                    try:
                        OrderText5.config(text=((PizzaOrder[0][4])))
                        OrderCost5.config(text=("${:,.2f}".format(float(PizzaOrder[1][4]))))
                        OrderBut5.place(x=870,y=317,height=20,width=27)
                        OrderText5.place(x=675,y=315)
                        OrderCost5.place(x=820,y=315)
                        OrderTextTot.place(x=675,y=355)
                        OrderCostTot.place(x=820,y=355) 
                    except:
                        OrderTextTot.place(x=675,y=315)
                        OrderCostTot.place(x=820,y=315)   
                except:
                    OrderTextTot.place(x=675,y=275)
                    OrderCostTot.place(x=820,y=275) 
            except:
                OrderTextTot.place(x=675,y=235)
                OrderCostTot.place(x=820,y=235)
        except:
            OrderTextTot.place(x=675,y=195)
            OrderCostTot.place(x=820,y=195)
    
    return

def RetFun(Win): 
    Win.destroy()
    return

def CheckFun(OrderType,PizzaOrder,Name,Address,Phone,ErrorText):
    if ((len(PizzaOrder[0]))<=(0)):
        ErrorText.config(text="Error No Pizzas")
    else:
        CostTot = CalcPizza(OrderType,PizzaOrder)
        SetDis(PizzaOrder,Name,Address,Phone,OrderType,CostTot)
    return

def CalcPizza(OrderType,PizzaOrder):
    CostDel = float(3)
    if OrderType == ("Delivery"):
        CostTot = CostDel
    else:
        CostTot = float(0)

    for main in range(len(PizzaOrder[0])):
        try:   
            CostTot+= (float(PizzaOrder[1][main]))
        except ValueError:
            print("Cost Err.")
    return(CostTot)

def SetDis(PizzaOrder,Name,Address,Phone,OrderType,CostTot):

    global Win2
    Win2.destroy()
    global Win3
    Win3.destroy()
    DateRaw = (datetime.now())
    Date = ((DateRaw).strftime("%d/%m/%y"))

    Win4 = Toplevel()
    Win4.geometry("493x275")
    Win4.config(bg=("#fff2cc"))
    Win4.title("Tony's Pizza Order Receipt")
    
    OrderBack = Label(Win4,text=(""),bg=("#cfe2f3"))
    
    SubText1 = Label(Win4,text=("Tony's Pizza"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 24"))
    SubText2 = Label(Win4,text=("Order Completed:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 13"))
    SubText3 = Label(Win4,text=("Order"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 24"))
    
    NameText = Label(Win4,text=("Name:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    NameBox = Label(Win4,text=(Name),bg=("#6fa8dc"),fg=("#ffffff"),anchor= N ,font=("{Trebuchet MS} 10"))

    if ((OrderType) == ("Delivery")):    
        PhonText = Label(Win4,text=("Phone No.:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        AddrText = Label(Win4,text=("Address:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        PhonBox = Label(Win4,text=(Phone),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))
        AddrBox = Label(Win4,text=(Address),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))
        PhonText.place(x=35,y=105)
        PhonBox.place(x=36,y=125,width=155,height=25)
        AddrText.place(x=35,y=160)
        AddrBox.place(x=36,y=180,width=155,height=25)

    DateText = Label(Win4,text=("Date:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    
    DateBox = Label(Win4,text=(Date),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 13"))
    RepBut = Button(Win4,text=("Enter Another Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RepFun())))
    Exit = Button(Win4,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(ExitFun())))
    OrderTotText = Label(Win4,text=("TOTAL:"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic bold"))
    OrderTotCost = Label(Win4,text=("${:,.2f}".format(CostTot)),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    try:
        Order1Text = Label(Win4,text=(PizzaOrder[0][0]),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order1Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][0]))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order2Text = Label(Win4,text=(PizzaOrder[0][1]),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order2Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][1]))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order3Text = Label(Win4,text=(PizzaOrder[0][2]),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order3Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][2]))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order4Text = Label(Win4,text=(PizzaOrder[0][3]),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order4Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][3]))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order5Text = Label(Win4,text=(PizzaOrder[0][4]),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order5Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][4]))),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    except:
        ()
   
    SubText1.place(x=30,y=10)
    SubText2.place(x=250,y=17)
    SubText3.place(x=305,y=50)
    OrderBack.place(x=250,y=50,height=170,width=213)
    NameText.place(x=35,y=50)
    NameBox.place(x=36,y=70,width=155,height=25)
 
    DateBox.place(x=388,y=17)
    RepBut.place(x=35,y=225,width=155,height=30)
    Exit.place(x=250,y=225,width=213,height=30)
    try:
        Order1Text.place(x=260,y=90) 
        Order1Cost.place(x=403,y=90) 
        Order2Text.place(x=260,y=110)
        Order2Cost.place(x=403,y=110)
        Order3Text.place(x=260,y=130)
        Order3Cost.place(x=403,y=130)
        Order4Text.place(x=260,y=150)
        Order4Cost.place(x=403,y=150)
        Order5Text.place(x=260,y=170)
        Order5Cost.place(x=403,y=170)
    except:
        ()
    OrderTotText.place(x=(260),y=(90+(20*(len(PizzaOrder[0])))))
    OrderTotCost.place(x=(403),y=(90+(20*(len(PizzaOrder[0])))))
    return

def RepFun():
    global PizzaOrder
    global OrderType
    
    try:
        global Win4
        Win4.destroy()
    except:
        ()
    OrderType = str("")
    PizzaOrder = [[]for main in range(2)]

    PizzaData = RetInfo()
    CustPage(PizzaData)
    return

PizzaData = RetInfo()
CustPage(PizzaData)