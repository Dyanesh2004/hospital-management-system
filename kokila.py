from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pymysql as m
win =Tk()
win.state('zoomed')
win.config(bg='black')
#=====================button function

def pd():


    x1=e1.get()
    x2=e2.get()
    x3=e3.get()
    x4=e4.get()
    x5=e5.get()
    x6=e6.get()
    x7=e7.get()
    x8=e8.get()
    x13=e13.get()
    x14=e14.get()
    x15=e15.get()

    if(x1=="" or x2=="" or x3=="" or x4=="" or x5=="" or x6=="" or x7=="" or x8=="" or x13=="" or x14=="" or x15==""):
        messagebox.showerror("message","all columns are required")

    else:
        try:

            con=m.connect(host="localhost",user="root",password="",database="host")
            z=con.cursor()
            z.execute("Insert into patient_dep values('"+x1+"','"+x2+"','"+x3+"','"+x5+"','"+x6+"','"+x7+"','"+x8+"','"+x13+"','"+x14+"','"+x15+"')")
            con.commit()
            messagebox.showinfo("message","registered sucessfully.....")



        except:

            messagebox.showerror("info","connection not established")



def delete():
    nameoftablets.set(""),
    ref.set(""),
    dose.set(""),
    issuedate.set(""),
    expdate.set(""),
    dailydose.set(""),
    nooftablets.set("")
    sideeffect.set(""),
    nameofpatient.set(""),
    dob.set(""),
    patientaddress.set("")
    bloodpressure.set("")
    storage.set("")
    meditation.set("")
    patientid.set("")
    frame1.delete("1.0",END)

def prescription():
    #txtPrescription.insert(END, 'Name of tablets: \t\t' + cnbNameTablets.get() + "\n")
    txt_frme.insert(END, 'Name of tablets: \t\t' + nameoftablets.get() +"\n")
    txt_frme.insert(END, 'Reference No.: \t\t' + ref.get() + "\n")
    txt_frme.insert(END, 'dose: \t\t' + dose.get() + "\n")
    txt_frme.insert(END, 'issuedate: \t\t' + issuedate.get() + "\n")
    txt_frme.insert(END, 'exp date: \t\t' + expdate.get() + "\n")
    txt_frme.insert(END, 'daily dose: \t\t' + dailydose.get() + "\n")
    txt_frme.insert(END, 'number of tablets: \t\t' + nooftablets.get() + "\n")
    txt_frme.insert(END, 'side effects: \t\t' + sideeffect.get() + "\n")
    txt_frme.insert(END, 'name of patient: \t\t' + nameofpatient.get() + "\n")
    txt_frme.insert(END, 'date of birth: \t\t' +  dob.get() + "\n")
    txt_frme.insert(END, 'blood pressure: \t\t' + bloodpressure.get() + "\n")
    txt_frme.insert(END, 'Storage advice: \t\t' + storage.get() + "\n")
    txt_frme.insert(END, 'mediation: \t\t' +meditation.get() + "\n")
    txt_frme.insert(END, 'patient Id: \t\t' + patientid.get() + "\n")

def view():
    table = ttk.Treeview(frame2, columns=('not', 'ref', 'dose', 'nots', 'issd', 'expd', 'dd', 'sd', 'pn', 'dob', 'pa'),xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set)

    table['columns'] = ('n', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9')

    table.column("#0", width=0, stretch=YES)
    table.column("n", anchor=CENTER, width=150)
    table.column("n1", anchor=CENTER, width=150)
    table.column("n2", anchor=CENTER, width=150)
    table.column("n3", anchor=CENTER, width=150)
    table.column("n4", anchor=CENTER, width=150)
    table.column("n5", anchor=CENTER, width=150)
    table.column("n6", anchor=CENTER, width=150)
    table.column("n7", anchor=CENTER, width=150)
    table.column("n8", anchor=CENTER, width=150)
    table.column("n9", anchor=CENTER, width=150)

    table.heading("n", text="Name_of_tablets", anchor=CENTER)
    table.heading("n1", text="Reference", anchor=CENTER)
    table.heading("n2", text="dose", anchor=CENTER)
    table.heading("n3", text="issue_date", anchor=CENTER)
    table.heading("n4", text="exp_date", anchor=CENTER)
    table.heading("n5", text="daily_dose", anchor=CENTER)
    table.heading("n6", text="side_effect", anchor=CENTER)
    table.heading("n7", text="patient_name", anchor=CENTER)
    table.heading("n8", text="dob", anchor=CENTER)
    table.heading("n9", text="patient_address", anchor=CENTER)

    db1 = m.connect(host="localhost", user="root", password="", db="host")
    cur = db1.cursor()
    cur.execute('select * from patient_dep')
    row = cur.fetchall()
    for i in row:
        table.insert(parent='', index='end', text='', values=(i))
    cur.close()
    db1.close()
    table.place(x=10, y=10)



def exit():
    Exit =messagebox.askyesno("Hospital Management Systems", "Confirm if you want to exit")
    if Exit > 0:
        win.destroy()
        from dyanesh import first_page
        return


#Heading
Label(win,text='hospital management system',font=('Arial',31),bg='blue',fg='white').pack(fill=X)
#frame1
frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1533,height=310)
#Label Frame for patient information
lf1=LabelFrame(frame1,text='Patient information',font=('Arial',15),bd=10,background='pink')
lf1.place(x=10,y=0,width=750,height=280)
#LAbels for patient information
Label(lf1,text='Name of Tablets',bg='pink').place(x=5,y=10)
Label(lf1,text='Reference No.',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose',bg='pink').place(x=5,y=70)
Label(lf1,text='No. of tablets',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text='Exp.Date',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effects',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Result',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Device',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient ID',bg='pink').place(x=370,y=100)
Label(lf1,text='Name of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address',bg='pink').place(x=370,y=190)
#Label frame for prescription
lf2=LabelFrame(frame1,text='Prescription',font=('Arial',15),bd=10)
lf2.place(x=770,y=0,width=450,height=280)


#textvariable for Entry field
nameoftablets=StringVar()
ref=StringVar()
dose=StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bloodpressure=StringVar()
storage=StringVar()
meditation=StringVar()
patientid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
patientaddress=StringVar()


#Entry field for all labels
e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)

e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)

e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)

e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=100,width=200)

e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)

e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)

e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)

e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=220,width=200)

e9=Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)

e10=Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)

e11=Entry(lf1,bd=4,textvariable=meditation)
e11.place(x=500,y=70,width=200)

e12=Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=500,y=100,width=200)

e13=Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=500,y=130,width=200)

e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)

e15=Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=500,y=190,width=200)

#frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1533,height=250)
#textbox for prescription
txt_frme=Text(lf2,font=('Arial',15),width=40,height=30,bg='yellow')
txt_frme.pack(fill=BOTH)


#Button
#delete button
d_btn =Button(win,text='Delete',font=('Arial',15),bg='brown',fg='white',bd=6,cursor='hand2',command=delete)
d_btn.place(x=0,y=600,width=270)
#prescription button
p_btn= Button(win,text='Prescription',font=('Arial',15),bg='purple',fg='white',bd=6,cursor='hand2',command=prescription)
p_btn.place(x=270,y=600,width=270)
#save Prescription Data
pd_btn =Button(win,text='save Prescription Data',font=('Arial',15),bg='green',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=540,y=600,width=270)
#clear button
c_btn =Button(win,text='Clear',font=('Arial',15),bg='blue',fg='white',bd=6,cursor='hand2')
c_btn.place(x=810,y=600,width=270)
#exit button
e_btn =Button(win,text='Exit',font=('Arial',15),bg='brown',fg='white',bd=6,cursor='hand2',command=exit)
e_btn.place(x=1080,y=600,width=270)
#database view button
d_btn =Button(win,text='view details',font=('Arial',15),bg='brown',fg='white',bd=6,cursor='hand2',command=view)
d_btn.place(x=1300,y=600,width=270)

#Scroll Bar for prescription Data
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')



mainloop()


#CREATE TABLE patient_dep(Name_of_tablets varchar(34), Reference varchar(34),dose varchar(34),issue_date varchar(34),exp_date varchar(34),daily_dose varchar(34),side_effect varchar(34),patient_name varchar(34),dob varchar(34),patient_address varchar (34))