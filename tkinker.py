import tkinter as t
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk,Image

a=t.Tk()
# a.geometry("1200x800")
a.title("hospital")
a.state('zoomed')
a.config(background="deeppink3")
image=Image.open("C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\doctor cartoon 1.png")
c=ImageTk.PhotoImage(image)
l=Label(a,image=c)
l.place(x=100,y=100)

def demo():
    x=t1.get()
    x1=t2.get()

    if(x=="dyanesh@gmail.com" or x1=="12345"):
        a.destroy()
        from dyanesh import first_page
    else:
        messagebox.showerror("message","eneter the mail id and password correctly")
l1=Label(a,text="welcone to my hospital database",font=("Lucida Calligraphy",35))
l1.place(x=400,y=25)

l2=Label(a,text="user name",font=("Lucida Calligraphy",35))
l2.place(x=890,y=200)

t1=Entry(a,foreground="black",font=("Lucida Calligraphy",35),width=10)
t1.place(x=1200,y=200)

l3=Label(a,text="password",font=("Lucida Calligraphy",35))
l3.place(x=890,y=300)

t2=Entry(a,foreground="black",font=("Lucida Calligraphy",35),width=10,show="*")
t2.place(x=1200,y=300)

b1=Button(a,text="submit",bg="grey",fg="black",font=("Lucida Calligraphy",35),command=demo)
b1.place(x=1100,y=400)

def show():
    image.config(file="C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\eye open image.png")
    t2.config(show="")
    q.config(command=hide)

def hide():
    image.config(file="C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\eye close image.png")
    t2.config(show="*")
    q.config(command=show)


image=PhotoImage(file="C:\\Users\\DYANESH\\Pictures\\Saved Pictures\\eye close image.png")
q=Button(a,image=image,command=show)
q.place(x=1470,y=300)








a.mainloop()
