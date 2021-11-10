
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
    Win1.geometry("360x360")
    Win1.config(bg="#fff2cc")

    SubTitle1 = Label(Win1,text="Tony's Pizza",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    PickBut = Button(Win1,text=("Pick Up"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(PickFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    DeliBut = Button(Win1,text=("Delivery"),fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(DeliFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))
    NameText = Label(Win1,text="Name:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    NameBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    AddrText = Label(Win1,text="Address:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    AddrBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    PhonText = Label(Win1,text="Phone No.:",fg=("#000000"),bg=("#fff2cc"),font =("{Trebuchet MS} 10 italic"))
    PhonBox = Entry(Win1,text="",fg=("#000000"),bg=("#cfe2f3"),font =("{Trebuchet MS} 10 italic"),state="disabled")
    ContBut = Button(Win1,text="Continue",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(ContFun(PizzaData,NameBox.get(),AddrBox.get(),PhonBox.get(),OrderType)))
    ExitBut = Button(Win1,text="Exit",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(ExitFun()))
    CleaBut = Button(Win1,text="Clear",fg=("#ffffff"),bg=("#6fa8dc"),font =("{Trebuchet MS} 10"),command=lambda:(CleaFun(PickBut,DeliBut,NameBox,AddrBox,PhonBox)))

    SubTitle1.pack()
    PickBut.pack()
    DeliBut.pack()
    NameText.pack()
    NameBox.pack()
    AddrText.pack()
    AddrBox.pack()
    PhonText.pack()
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

def ContFun(PizzaData,Name,Address,Phone,OrderType):
    if ((OrderType) == ("Pick Up")):
        if Name == "":
            print("Error in Name")
        else:
            MenuPage(PizzaData,OrderType,Name,Address,Phone)
    elif ((OrderType) == ("Delivery")):
        if Name == "":
            print("Error in Name")
        elif Address == "":
            print("Error in Address")
        elif Phone =="":
            print("Error in Phone")
        else:
            MenuPage(PizzaData,OrderType,Name,Address,Phone)
    else:
        print("Error in Order Type")
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
    Win2.geometry("360x720")
    Win2.config(bg="#fff2cc")

    SubText1 = Label(Win2,text="Tony's Pizza",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    SubText2 = Label(Win2,text = "Standard Pizzas",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic")) 
    SubText3 = Label(Win2,text=("Gourmet Pizzas"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))

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

    OrderText = Label(Win2,text=("Order"),bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText1 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText2 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText3 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText4 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderText5 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost1 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost2 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost3 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost4 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    OrderCost5 = Label(Win2,text="",bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    
    OrderBut1 = Button(Win2,text="X",bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(0,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    OrderBut2 = Button(Win2,text="X",bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(1,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    OrderBut3 = Button(Win2,text="X",bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(2,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    OrderBut4 = Button(Win2,text="X",bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(3,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    OrderBut5 = Button(Win2,text="X",bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:SubFun(4,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    
    Pizza1But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,0,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza2But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,1,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza3But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,2,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza4But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,3,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza5But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,4,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza6But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,5,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza7But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,6,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza8But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,7,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza9But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,8,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza10But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,9,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza11But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,10,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    Pizza12But = Button(Win2,text=("View More"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:PopOutFun(PizzaData,11,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))


    ExitBut = Button(Win2,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:(ExitFun()))
    OrderBack = Label(Win2,text=(""),bg=("#cfe2f3"))

    CheckBut = Button(Win2,text=("Checkout"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:CheckFun(OrderType,PizzaOrder,Name,Address,Phone)))
    CanBut = Button(Win2,text=("Cancel"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RepFun())))

    SubText1.pack()
    SubText2.pack()

    Pizza1Text.pack()
    Pizza1But.pack()   
    Pizza2Text.pack()
    Pizza2But.pack()   
    Pizza3Text.pack()
    Pizza3But.pack()
    Pizza4Text.pack()
    Pizza4But.pack()
    Pizza5Text.pack()
    Pizza5But.pack()
    Pizza6Text.pack()
    Pizza6But.pack()
    Pizza7Text.pack()
    Pizza7But.pack()
    SubText3.pack()
    Pizza8Text.pack()
    Pizza8But.pack()
    Pizza9Text.pack()
    Pizza9But.pack()
    Pizza10Text.pack()
    Pizza10But.pack()
    Pizza11Text.pack()
    Pizza11But.pack()
    Pizza12Text.pack()
    Pizza12But.pack()

    ExitBut.pack()
    OrderBack.place(x=40,y=40,height="320",width="320")
    OrderText1.pack()
    OrderText2.pack()
    OrderText3.pack()
    OrderText4.pack()
    OrderText5.pack()
    OrderCost1.pack()
    OrderCost2.pack()
    OrderCost3.pack()
    OrderCost4.pack()
    OrderCost5.pack()
    CheckBut.pack()
    CanBut.pack()
    return

def SubFun(OrderPos,PizzaOrder,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5):
    if ((len(PizzaOrder[0]))<=0):
        print("Error No pizzas")
    elif ((len(PizzaOrder[0]))<=(OrderPos)):
        print("Error No Pizza in order slot")
    else:
        PizzaOrder[0].pop(OrderPos)
        PizzaOrder[1].pop(OrderPos)
        if ((len(PizzaOrder[0]))==0):
            OrderText1.config(text=(""))
            OrderBut1.pack_forget()
        elif ((len(PizzaOrder[0]))==1):
            OrderText1.config(text=(PizzaOrder[0][0]))
            OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
            OrderText2.config(text=(""))
            OrderCost2.config(text=(""))
            OrderBut2.pack_forget()
            OrderCost2.pack_forget()
        elif ((len(PizzaOrder[0]))==2):
            OrderText1.config(text=(PizzaOrder[0][0]))
            OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
            OrderText2.config(text=(PizzaOrder[0][1]))
            OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][1]))))
            OrderText3.config(text=(""))
            OrderCost3.config(text=(""))
            OrderBut3.pack_forget()
            OrderCost3.pack_forget()
        elif ((len(PizzaOrder[0]))==3):
            OrderText1.config(text=(PizzaOrder[0][0]))
            OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
            OrderText2.config(text=(PizzaOrder[0][1]))
            OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][1]))))
            OrderText3.config(text=(PizzaOrder[0][2]))
            OrderCost3.config(text=("${:,.2f}".format(float(PizzaOrder[1][2]))))
            OrderText4.config(text=(""))
            OrderCost4.config(text=(""))
            OrderBut4.pack_forget()
            OrderCost4.pack_forget()
        elif ((len(PizzaOrder[0]))==4):
            OrderText1.config(text=(PizzaOrder[0][0]))
            OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][0]))))
            OrderText2.config(text=(PizzaOrder[0][1]))
            OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][1]))))
            OrderText3.config(text=(PizzaOrder[0][2]))
            OrderCost3.config(text=("${:,.2f}".format(float(PizzaOrder[1][2]))))
            OrderText4.config(text=(PizzaOrder[0][3]))
            OrderCost4.config(text=("${:,.2f}".format(float(PizzaOrder[1][3]))))
            OrderText5.config(text=(""))
            OrderCost5.config(text=(""))
            OrderBut5.pack_forget()
            OrderCost5.pack_forget()
        else:
            print("Error in logic 1")
    return

def PopOutFun(PizzaData,PizzaNum,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5):
    try:
        global Win3
        Win3.destroy()
    except:
        ()

    if (PizzaData[PizzaNum][1] == "8.5"):
        PizzaType = str("Standard ")
    elif (PizzaData[PizzaNum][1]) == "13.5":
        PizzaType =str("Gourmet")

    Win3 = Toplevel()
    Win3.geometry("360x360")
    Win3.config(bg="#fff2cc")

    TitleText = Label(Win3,text=("Tony's Pizza"),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))
    SubText1 = Label(Win3,text=(PizzaData[PizzaNum][0]),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic")) 
    PizzaText1 = Label(Win3,text=(PizzaType),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))
    PizzaText2 = Label(Win3,text=("${:,.2f}".format(float(PizzaData[PizzaNum][1]))),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))
    PizzaInfoText = Label(Win3,text=(PizzaData[PizzaNum][2]),bg=("#fff2cc"),font=("{Trebuchet MS} 10 italic"))

    AddBut = Button(Win3,text=("Add to Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:AddFun(len(PizzaOrder[0]),PizzaData,PizzaNum,AddBox.get(),OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5))
    AddBox = Entry(Win3,bg=("#cfe2f3"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    AddBox.insert(END,1)
    Exit = Button(Win3,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=lambda:ExitFun())
    RetBut = Button(Win3,text=("Return to Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RetFun(Win3))))

    TitleText.pack()
    SubText1.pack()
    PizzaText1.pack()
    PizzaText2.pack()
    PizzaInfoText.pack()
    AddBox.pack()
    AddBut.pack()
    Exit.pack()
    RetBut.pack()
    return

def AddFun(PizzaOrderSize,PizzaData,PizzaNum,PizzaQt,OrderText1,OrderText2,OrderText3,OrderText4,OrderText5,OrderBut1,OrderBut2,OrderBut3,OrderBut4,OrderBut5,OrderCost1,OrderCost2,OrderCost3,OrderCost4,OrderCost5):
    global PizzaOrder
    try:
        PizzaQt=int(PizzaQt)
        if ((PizzaQt)<=0):
            print("Error Invalid Qt.")
        elif ((PizzaOrderSize+PizzaQt)>=(6)):
            print("Error 5 pizza max.")
        else:            
            PizzaOrder[0].append(PizzaData[PizzaNum][0])
            PizzaOrder[1].append(PizzaData[PizzaNum][1])
            if(PizzaOrderSize==0):
                OrderText1.config(text=((PizzaOrder[0][PizzaOrderSize])))
                OrderCost1.config(text=("${:,.2f}".format(float(PizzaOrder[1][PizzaOrderSize]))))
                OrderBut1.pack()
            elif(PizzaOrderSize==1):
                OrderText2.config(text=((PizzaOrder[0][PizzaOrderSize])))
                OrderCost2.config(text=("${:,.2f}".format(float(PizzaOrder[1][PizzaOrderSize]))))
                OrderBut2.pack()
            elif(PizzaOrderSize==2):
                OrderText3.config(text=((PizzaOrder[0][PizzaOrderSize])))
                OrderCost3.config(text=("${:,.2f}".format(float(PizzaOrder[1][PizzaOrderSize]))))
                OrderBut3.pack()
            elif(PizzaOrderSize==3):
                OrderText4.config(text=((PizzaOrder[0][PizzaOrderSize])))
                OrderCost4.config(text=("${:,.2f}".format(float(PizzaOrder[1][PizzaOrderSize]))))
                OrderBut4.pack()
            elif(PizzaOrderSize==4):
                OrderText5.config(text=((PizzaOrder[0][PizzaOrderSize])))
                OrderCost5.config(text=("${:,.2f}".format(float(PizzaOrder[1][PizzaOrderSize]))))
                OrderBut5.pack()
    except ValueError:
        print("Error Invalid Qt.")
    return

def RetFun(Win):
    
    Win.destroy()
    return

def CheckFun(OrderType,PizzaOrder,Name,Address,Phone):
    if ((len(PizzaOrder[0]))<=(0)):
        print("Error No Pizzas Ordered")
    else:
        CostTot = CalcPizza(OrderType,PizzaOrder)
        SetDis(PizzaOrder,Name,Address,Phone,OrderType,CostTot)
    return

def CalcPizza(OrderType,PizzaOrder):
    
    if OrderType == ("Delivery"):
        CostTot = float(3)
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
    print(PizzaOrder)
    DateRaw = (datetime.now())
    Date = ((DateRaw).strftime("%d/%m/%y"))

    Win4 = Toplevel()
    Win4.geometry("720x720")
    Win4.config(bg=("#fff2cc"))

    SubText1 = Label(Win4,text=("Tony's Pizza"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    SubText2 = Label(Win4,text=("Order Completed"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    SubText3 = Label(Win4,text=("Order"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    NameText = Label(Win4,text=("Name:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    NameBox = Label(Win4,text=(Name),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))

    if ((OrderType) == ("Delivery")):    
        PhonText = Label(Win4,text=("Phone No.:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        AddrText = Label(Win4,text=("Address:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        PhonBox = Label(Win4,text=(Phone),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))
        AddrBox = Label(Win4,text=(Address),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))

    DateText = Label(Win4,text=("Date:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
    
    DateBox = Label(Win4,text=(Date),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"))
    RepBut = Button(Win4,text=("Enter Another Order"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(RepFun())))
    Exit = Button(Win4,text=("Exit"),bg=("#6fa8dc"),fg=("#ffffff"),font=("{Trebuchet MS} 10"),command=(lambda:(ExitFun())))
    OrderTotText = Label(Win4,text=("TOTAL:"),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
    OrderTotCost = Label(Win4,text=("${:,.2f}".format(CostTot)),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
    try:
        Order1Text = Label(Win4,text=(PizzaOrder[0][0]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order1Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][0]))),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
        Order2Text = Label(Win4,text=(PizzaOrder[0][1]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order2Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][1]))),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
        Order3Text = Label(Win4,text=(PizzaOrder[0][2]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order3Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][2]))),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
        Order4Text = Label(Win4,text=(PizzaOrder[0][3]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order4Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][3]))),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
        Order5Text = Label(Win4,text=(PizzaOrder[0][4]),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10 italic"))
        Order5Cost = Label(Win4,text=("${:,.2f}".format(float(PizzaOrder[1][4]))),bg=("#fff2cc"),fg=("#000000"),font=("{Trebuchet MS} 10"))
    except:
        ()
   
    SubText1.pack()
    SubText2.pack()
    NameText.pack()
    NameBox.pack()
    try:
        PhonText.pack()
        PhonBox.pack()
        AddrText.pack()
        AddrBox.pack()
    except:
        ()
    DateText.pack()
    DateBox.pack()
    RepBut.pack()
    Exit.pack()
    try:
        Order1Text.pack() 
        Order1Cost.pack()
        Order2Text.pack()
        Order2Cost.pack()
        Order3Text.pack()
        Order3Cost.pack()
        Order4Text.pack()
        Order4Cost.pack()
        Order5Text.pack()
        Order5Cost.pack()
    except:
        ()
    OrderTotText.pack()
    OrderTotCost.pack()
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