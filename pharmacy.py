import tkinter as t
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql as m

a=t.Tk()
a.state('zoomed')
a.title("pharmacy")
a.config(background="green")


Label(a,text='pharmacy management system',font=('Arial',31),bg='blue',fg='white').pack(fill=X)

frame1 = Frame(a,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1533,height=330)
lf1=LabelFrame(frame1,text='customer information',font=('Arial',15),bd=10,background='pink')
lf1.place(x=10,y=0,width=750,height=310)

# frame2 = Frame(a,bd=15,relief=RIDGE,background="yellow")
# frame2.place(x=800,y=65,width=1133,height=310)
# lf2=LabelFrame(frame1,text='prescription',font=('Arial',15),bd=10,background='pink')
# lf2.place(x=800,y=0,width=750,height=310)

lf2=LabelFrame(frame1,text='Prescription',font=('Arial',15),bd=10)
lf2.place(x=770,y=0,width=450,height=280)
txt_frme=Text(lf2,font=('Arial',15),width=40,height=30,bg='yellow')
txt_frme.pack(fill=BOTH)


nameoftablets=StringVar()
drname=StringVar()
hospitalname=StringVar()
age=StringVar()
mobilenumber=StringVar()

def prescription():
    x1=e1.get()
    x2=e2.get()
    x3=e3.get()
    x4=e4.get()
    x5=e5.get()
    if(x1=="" or x2=="" or x3=="" or x4=="" or x5==""):
        messagebox.showerror("message","all fields are required ")
    else:
        txt_frme.insert(END, 'Name of tablets: \t\t' + nameoftablets.get() + "\n")
        txt_frme.insert(END, 'Reference No.: \t\t' + drname.get() + "\n")
        txt_frme.insert(END, 'dose: \t\t' + hospitalname.get() + "\n")
        txt_frme.insert(END, 'issuedate: \t\t' + age.get() + "\n")
        txt_frme.insert(END, 'exp date: \t\t' + mobilenumber.get() + "\n")

def reset():
    nameoftablets.set(""),
    drname.set(""),
    hospitalname.set(""),
    age.set(""),
    mobilenumber.set(""),
    frame1.delete("1.0", END)

def submit():
    x1 = e1.get()
    x2 = e2.get()
    x3 = e3.get()
    x4 = e4.get()
    x5 = e5.get()
    if (x1 == "" or x2 == "" or x3 == "" or x4 == "" or x5 == ""):
        messagebox.showerror("message", "all fields are required ")
    else:

            con=m.connect(host="localhost",user="root",password="",database="pharmacy")
            z=con.cursor()
            z.execute("Insert into customer_details values('"+x1+"','"+x2+"','"+x3+"','"+x4+"','"+x5+"')")
            con.commit()
            messagebox.showinfo("message","registered sucessfully.........")


def exit():
    Exit = messagebox.askyesno("Hospital Management Systems", "Confirm if you want to exit")
    if Exit > 0:
        a.destroy()
        from dyanesh import first_page


def view_details():
   # table = ttk.Treeview(frame2, columns=('name_of_tablets', 'doctor_name', 'hospital_name', 'age', 'mobile_number'),xscrollcommand=scroll_y.0, yscrollcommand=scroll_x.set)
    table=ttk.Treeview(a)
    table['columns'] = ('n', 'n1', 'n2', 'n3', 'n4')

    table.column("#0", width=0, stretch=YES)
    table.column("n", anchor=CENTER, width=300)
    table.column("n1", anchor=CENTER, width=300)
    table.column("n2", anchor=CENTER, width=300)
    table.column("n3", anchor=CENTER, width=300)
    table.column("n4", anchor=CENTER, width=300)


    table.heading("n", text="Name_of_tablets", anchor=CENTER)
    table.heading("n1", text="doctor_name", anchor=CENTER)
    table.heading("n2", text="hospital_name", anchor=CENTER)
    table.heading("n3", text="age", anchor=CENTER)
    table.heading("n4", text="mobile_number", anchor=CENTER)


    db1 = m.connect(host="localhost", user="root", password="", db="pharmacy")
    cur = db1.cursor()
    cur.execute('select * from customer_details')
    row = cur.fetchall()
    for i in row:
        table.insert(parent='', index='end', text='', values=(i))
    cur.close()
    db1.close()
    table.place(x=17, y=585)


#labels for pharmacy
Label(lf1,text='Name of Tablets',bg='pink',font=("Arial",20)).place(x=5,y=10)
Label(lf1,text='doctor name.',bg='pink',font=("Arial",20)).place(x=5,y=55)
Label(lf1,text='hospital name',bg='pink',font=("Arial",20)).place(x=5,y=100)
Label(lf1,text='age',bg='pink',font=("Arial",20)).place(x=5,y=150)
Label(lf1,text='mobile number',bg='pink',font=("Arial",20)).place(x=5,y=200)

#entry boxes for pharmacy
e1=Entry(a,foreground="black",font=("Arial",20),width=20,textvariable=nameoftablets)
e1.place(x=300,y=100)

e2=Entry(a,foreground="black",font=("Arial",20),width=20,textvariable=drname)
e2.place(x=300,y=150)

e3=Entry(a,foreground="black",font=("Arial",20),width=20,textvariable=hospitalname)
e3.place(x=300,y=200)

e4=Entry(a,foreground="black",font=("Arial",20),width=20,textvariable=age)
e4.place(x=300,y=250)

e5=Entry(a,foreground="black",font=("Arial",20),width=20,textvariable=mobilenumber)
e5.place(x=300,y=300)

#buttons
b1=Button(a,text="reset", bg="violet",fg="green",font=("Calibri",40),width=10,command=reset)
b1.place(x=0,y=400)

b2=Button(a,text="submit",bg="violet",fg="green",font=("Calibri",40),width=10,command=submit)
b2.place(x=300,y=400)

b3=Button(a,text="prescription",bg="violet",fg="green",font=("Calibri",40),width=10,command=prescription)
b3.place(x=600,y=400)

b4=Button(a,text="view details",bg="violet",fg="green",font=("Calibri",40),width=10,command=view_details)
b4.place(x=900,y=400)

b5=Button(a,text="exit",bg="violet",fg="green",font=("Calibri",40),width=10,command=exit)
b5.place(x=1200,y=400)

frame2=Frame(a,bd=15,relief=RIDGE)
frame2.place(x=0,y=560,width=1533,height=250)

# txt_frme=Text(,font=('Arial',15),width=40,height=30,bg='yellow')
# txt_frme.pack(fill=BOTH)

a.mainloop()