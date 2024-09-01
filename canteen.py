from tkinter import *
#from tkinter import messagebox

root=Tk()
root.geometry("3000x2000")
root.title("Bill management")


def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_coffee.delete(0,END)
    entry_tea.delete(0,END)

    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_eggs.delete(0,END)

def exit():
    root.destroy()
    from dyanesh import first_page
def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(coffee.get())
    except: a3=0

    try:a4=int(tea.get())
    except: a4=0

    try:a5=int(juice.get())
    except: a5=0

    try:a6=int(pancakes.get())
    except: a6=0

    try:a7=int(eggs.get())
    except: a7=0

    #cost of each item
    c1 = 15 * a1
    c2 = 10 * a2
    c3 = 10 * a3
    c4 = 12 * a4
    c5 = 20 * a5
    c6 = 25 * a6
    c7 = 15 * a7

    #total_bill = c1 + c2 + c3 + c4 + c5 + c6 + c7
    #messagebox.showinfo("Total Bill", f"Your total bill is Rs. {total_bill}")

    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)


Label(text="Bill management", bg="black", fg="white", font=("Sitka Text Semibold",45),width="300", height="2").pack()

#menu card
f=Frame(root,bg="green",highlightcolor="black", highlightthickness=1, width=500, height=580)
f.place(x=10,y=200)

Label(f,text="Menu", font=("Sitka Text Semibold",40),fg="black",bg="yellow").place(x=125,y=10)


Label(f,text="dosa.........Rs.15/plate", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=100)
Label(f,text="cookies.........Rs.10", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=150)
Label(f,text="tea.........Rs.10", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=200)
Label(f,text="coffee.........Rs.12", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=250)
Label(f,text="juice.........Rs.20", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=300)
Label(f,text="pancakes.........Rs.25", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=350)
Label(f,text="eggs.........Rs.15", font=("Lucida Calligraphy",25),fg="black",bg="green").place(x=10,y=400)


#bill
f2=Frame(root,bg="yellow",highlightbackground="black",highlightthickness=1,width=500,height=550)
f2.place(x=1000,y=200)

Bill=Label(f2,text="Bill",font=("Californian FB",40),bg="yellow",fg="black")
Bill.place(x=200,y=10)

#entry work
f1=Frame(root,bd=5,height=580,width=500,relief=RAISED)
f1.place(x=550,y=200)

dosa=StringVar()
cookies=StringVar()
tea=StringVar()
coffee=StringVar()
juice=StringVar()
pancakes=StringVar()
eggs=StringVar()
Total_bill=StringVar()



#label
lbl_dosa=Label(f1,font=("aria",25),text="Dosa",width=12,fg="blue")
lbl_cookies=Label(f1,font=("aria",25),text="cookies",width=12,fg="blue")
lbl_tea=Label(f1,font=("aria",25),text="tea",width=12,fg="blue")
lbl_coffee=Label(f1,font=("aria",25),text="coffee",width=12,fg="blue")
lbl_juice=Label(f1,font=("aria",25),text="juice",width=12,fg="blue")
lbl_pancakes=Label(f1,font=("aria",25),text="pancakes",width=12,fg="blue")
lbl_eggs=Label(f1,font=("aria",25),text="eggs",width=12,fg="blue")

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)



#entry
entry_dosa=Entry(f1,font=("aria",20),textvariable=dosa,bd=6,width=8,bg="pink")
entry_cookies=Entry(f1,font=("aria",20),textvariable=cookies,bd=6,width=8,bg="pink")
entry_tea=Entry(f1,font=("aria",20),textvariable=tea,bd=6,width=8,bg="pink")
entry_coffee=Entry(f1,font=("aria",20),textvariable=coffee,bd=6,width=8,bg="pink")
entry_juice=Entry(f1,font=("aria",20),textvariable=juice,bd=6,width=8,bg="pink")
entry_pancakes=Entry(f1,font=("aria",20),textvariable=pancakes,bd=6,width=8,bg="pink")
entry_eggs=Entry(f1,font=("aria",20),textvariable=eggs,bd=6,width=8,bg="pink")

entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_tea.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_juice.grid(row=5,column=1)
entry_pancakes.grid(row=6,column=1)
entry_eggs.grid(row=7,column=1)











#button
btn_reset=Button(f1,bd=5,fg="black",bg="blue",font=("ariel",16),width=10,text="reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16),width=10,text="total",command=Total)
btn_total.grid(row=8,column=1)

btn_exit=Button(f1,bd=5,fg="black",bg="orange",font=("ariel",16),width=10,text="exit",command=exit)
btn_exit.grid(row=9,column=1)

root.mainloop()

