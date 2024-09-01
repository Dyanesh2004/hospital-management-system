import tkinter as t
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image

a=t.Tk()
a.state('zoomed')
a.title("first page")
a.config(background="violet")
# image=Image.open("C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\logo 3 edit.png")
# c=ImageTk.PhotoImage(image)
# l=Label(a,image=c)
# l.place(x=20,y=40)

image=Image.open("C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\logo 2 edit.png")
c1=ImageTk.PhotoImage(image)
l=Label(a,image=c1)
l.place(x=800,y=40)

# def cab():
#     a.destroy()
#     from dyanesh import cab
def canteen():
    a.destroy()
    from dyanesh import canteen

def hospital():
    a.destroy()
    from dyanesh import kokila


def game():

    import flappy_bird


def pharmacy():
    a.destroy()
    from dyanesh import pharmacy

def exit():
    messagebox.askyesno("message","do you want to exit?")
    a.destroy()

b1=Button(a,text="hopital management system",font=("Centaur",30),background="maroon",foreground="white",width=30,height=0,command=hospital)
b1.place(x=100,y=200)

b2=Button(a,text="pharmacy management system",font=("Centaur",30),background="blue",foreground="white",width=30,height=0,command=pharmacy)
b2.place(x=100,y=300)

b3=Button(a,text="canteen",font=("Centaur",30),background="green",foreground="white",width=30,height=0,command=canteen)
b3.place(x=100,y=400)

b4=Button(a,text="play games for children",font=("Centaur",30),background="orange",foreground="white",width=30,height=0,command=game)
b4.place(x=100,y=500)

b5=Button(a,text="exit",font=("Centaur",30),background="pink",foreground="white",width=30,height=0,command=exit)
b5.place(x=100,y=600)

# b6=Button(a,text="cab booking system",font=("Centaur",30),background="black",foreground="white",width=30,height=0)
# b6.place(x=100,y=100)
a.mainloop()