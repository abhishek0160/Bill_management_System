from tkinter import*
import tkinter
top=Tk()

top.title("BILL MANAGMENT")
top.geometry("1400x600")

lbltitle=Label(top,text="BIG BITES FAST FOOD",bg="light green",fg="brown",bd=20,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
lbltitle.pack(side=TOP,fill=X)
###MENU###
DataFrameLeft=LabelFrame(top,text="MENU",bg="light pink",fg="green",bd=20,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameLeft.place(x=2,y=97,width=455,height=350)
member2=Label(DataFrameLeft,text="MENU",bg="light pink",font=("times new roman",15,"bold"),padx=2,pady=6)

lb1=Label(DataFrameLeft,text="Chola bhutra...........R.s.80/plate",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=0,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Chow main...........R.s.40/plate",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=1,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Sandwich...........R.s.50/pic",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=2,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Pizza...........R.s.90/pic",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=3,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Burger...........R.s.45/pic",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=4,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Pasta...........R.s.60/plate",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=5,column=0,sticky=W)

lb1=Label(DataFrameLeft,text="Bread pakora...........R.s.20/pics",bg="light pink",font=("timesnew roman",15,"bold"),padx=2,pady=6)
Height1=StringVar()
lb1.grid(row=6,column=0,sticky=W)

###TOTAL ITEMS###
DataFrameLeft=LabelFrame(top,text="TOTAL ITEMS",bg="light pink",fg="green",bd=20,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameLeft.place(x=455,y=97,width=455,height=350)
member2=Label(DataFrameLeft,text="TOTAL ITEMS",bg="light pink",font=("times new roman",15,"bold"),padx=2,pady=6)


Cholabhutra=StringVar()
Chowmain=StringVar()
Sandwich=StringVar()
Pizza=StringVar()
Burger=StringVar()
Pasta=StringVar()
Breadpakora=StringVar()

lbl_Cholabhutra=Label(DataFrameLeft,font=("aria",15,'bold'),text="Cholabhutra",width=12,fg="blue",bg="light pink")
lbl_Cholabhutra.grid(row=1,column=1)
entry_Cholabhutra=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Cholabhutra,bd=4,width=8,bg="light pink")
entry_Cholabhutra.grid(row=1,column=2)
entry_Cholabhutra.insert(0,"0")

lbl_Chowmain=Label(DataFrameLeft,font=("aria",15,'bold'),text="Chowmain",width=12,fg="blue",bg="light pink")
lbl_Chowmain.grid(row=2,column=1)
entry_Chowmain=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Chowmain,bd=4,width=8,bg="light pink")
entry_Chowmain.grid(row=2,column=2)
entry_Chowmain.insert(0,"0")

lbl_Sandwich=Label(DataFrameLeft,font=("aria",15,'bold'),text="Sandwich",width=12,fg="blue",bg="light pink")
lbl_Sandwich.grid(row=3,column=1)
entry_Sandwich=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Sandwich,bd=4,width=8,bg="light pink")
entry_Sandwich.grid(row=3,column=2)
entry_Sandwich.insert(0,"0")

lbl_Pizza=Label(DataFrameLeft,font=("aria",15,'bold'),text="Pizza",width=12,fg="blue",bg="light pink")
lbl_Pizza.grid(row=4,column=1)
entry_Pizza=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Pizza,bd=4,width=8,bg="light pink")
entry_Pizza.grid(row=4,column=2)
entry_Pizza.insert(0,"0")
                      
lbl_Burger=Label(DataFrameLeft,font=("aria",15,'bold'),text="Burger",width=12,fg="blue",bg="light pink")
lbl_Burger.grid(row=5,column=1)
entry_Burger=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Burger,bd=4,width=8,bg="light pink")
entry_Burger.grid(row=5,column=2)
entry_Burger.insert(0,"0")

lbl_Pasta=Label(DataFrameLeft,font=("aria",15,'bold'),text="Pasta",width=12,fg="blue",bg="light pink")
lbl_Pasta.grid(row=6,column=1)
entry_Pasta=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Pasta,bd=4,width=8,bg="light pink")
entry_Pasta.grid(row=6,column=2)
entry_Pasta.insert(0,"0")

lbl_Breadpakora=Label(DataFrameLeft,font=("aria",15,'bold'),text="Breadpakora",width=12,fg="blue",bg="light pink")
lbl_Breadpakora.grid(row=7,column=1)
entry_Breadpakora=Entry(DataFrameLeft,font=("aria",15,'bold'),textvariable=Breadpakora,bd=4,width=8,bg="light pink")
entry_Breadpakora.grid(row=7,column=2)
entry_Breadpakora.insert(0,"0")
def abc():
    s=()
    s=int(entry_Cholabhutra.get())*80
    l1=Label(DataFrameLeft,text="Cholabhutra",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=7,column=2)
    l=Label(DataFrameLeft,text=s,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=7,column=5)
    t=()
    t=int(entry_Chowmain.get())*40
    l1=Label(DataFrameLeft,text="Chowmain",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=8,column=2)
    l=Label(DataFrameLeft,text=t,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=8,column=5)

    d=()
    d=int(entry_Sandwich.get())*50
    l1=Label(DataFrameLeft,text="Sandwich",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=9,column=2)
    l=Label(DataFrameLeft,text=d,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=9,column=5)

    e=()
    e=int(entry_Pizza.get())*90
    l1=Label(DataFrameLeft,text="Pizza",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=10,column=2)
    l=Label(DataFrameLeft,text=e,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=10,column=5)

    f=()
    f=int(entry_Burger.get())*45
    l1=Label(DataFrameLeft,text="Burger",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=11,column=2)
    l=Label(DataFrameLeft,text=f,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=11,column=5)

    g=()
    g=int(entry_Pasta.get())*60
    l1=Label(DataFrameLeft,text="Pasta",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=12,column=2)
    l=Label(DataFrameLeft,text=g,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=12,column=5)

    h=()
    h=int(entry_Breadpakora.get())*20
    l1=Label(DataFrameLeft,text="Breadpakora\t",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l1.grid(row=13,column=2)
    l=Label(DataFrameLeft,text=h,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l.grid(row=13,column=5)
    
    l=Label(DataFrameLeft,text="Total",bg="lightpink",bd=0,fg="blue",relief=RIDGE,font=("times new roman",15,"bold"))
    l.grid(row=14,column=2)
    
    Total=s+t+d+e+f+g+h

    l0=Label(DataFrameLeft,text=Total,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
    l0.grid(row=14,column=5)

    def tt():
        root=Toplevel(DataFrameLeft)
        
        root.title("BILL MANAGMENT")
        root.geometry("400x600")
        p=Frame(root,width="400",height="600",bg="lightpink").place(x=0,y=0)
        lbltitle=Label(root,text="BIG BITES FAST FOOD",bg="light green",fg="brown",bd=20,relief=RIDGE,font=("times new roman",16,"bold"),padx=65,pady=6)
        lbltitle.place(x=0,y=0)

        l1=Label(root,text="Cholabhutra",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=120)
        l=Label(root,text=s,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=120)

        l1=Label(root,text="Chowmain",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=150)
        l=Label(root,text=t,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=150)

        l1=Label(root,text="Sandwich",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=180)
        l=Label(root,text=d,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=180)

        l1=Label(root,text="Pizza",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=210)
        l=Label(root,text=e,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=210)


        l1=Label(root,text="Burger",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=240)
        l=Label(root,text=f,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=240)

        l1=Label(root,text="Pasta",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=270)
        l=Label(root,text=g,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=270)        

        l1=Label(root,text="Breadpakora",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=300)
        l=Label(root,text=h,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=300)

        l1=Label(root,text="Total",bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l1.place(x=10,y=350)
        l=Label(root,text=Total,bg="lightpink",fg="black",font=("timesnew roman",15,"bold"))
        l.place(x=300,y=350)

        l1=Label(root,text="THANKU FOR ORDER",bg="lightpink",fg="brown",font=("timesnew roman",18,"bold"))
        l1.place(x=70,y=400)



        root.mainloop()


    

    l=Button(DataFrameLeft,text="Print",bg="lightpink",fg="blue",command=tt,bd=8,relief=RIDGE,font=("times new roman",10,"bold"))
    l.grid(row=15,column=3)


b=Button(DataFrameLeft,text="Calculate",bg="lightpink",fg="blue",bd=8,relief=RIDGE,font=("times new roman",10,"bold"),command=abc)
b.grid(row=10,column=2)

###BILL###
DataFrameLeft=LabelFrame(top,text="BILL",bg="lightpink",fg="green",bd=20,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameLeft.place(x=910,y=97,width=455,height=350)
member2=Label(DataFrameLeft,text="BILL",bg="light pink",font=("times new roman",15,"bold"),padx=2,pady=6)

top.mainloop()