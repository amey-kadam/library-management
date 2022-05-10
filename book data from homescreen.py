from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from typing import Sized 
from PIL import Image,ImageTk
import random
import sqlite3 

bkd = Tk()
bkd.title("Book Data")
bkd.geometry("1280x1920")
bkd.state('zoomed')
c3 = Canvas(bkd,background="black",width=300,height=390)
c3.place(x=570,y=40)
C3=Canvas(bkd,width=1280,height=1920)
C3.pack()
image3=Image.open("C:\\Users\\ameyp\\Downloads\\download2.png")
resize_image3 = image3.resize((1470,700))
img3=ImageTk.PhotoImage(resize_image3)
C3.create_image(-70,0,anchor=NW,image=img3)      

Button(bkd,text="Add Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=50)

Button(bkd,text="Search Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50, y=150)

Button(bkd,text="All Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=250)

Button(bkd,text="Main Menu",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=350)

    

Label(bkd,text="Book ID :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=60)

Label(bkd,text="Title :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=110)

Label(bkd,text="Author :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=160)

Label(bkd,text="Genre :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=210)

Label(bkd,text="Copies :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=260)

Label(bkd,text="Location :",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=310)


book_id1 = Entry(bkd,background='honeydew')
book_id1.place(x=720,y=60)
titlee1 = Entry(bkd,background='honeydew')
titlee1.place(x=720,y=110)
autho1 = Entry(bkd,background='honeydew')
autho1.place(x=720,y=160)
gene1 = Entry(bkd,background='honeydew')
gene1.place(x=720,y=210)
cpy1 = Entry(bkd,background='honeydew')
cpy1.place(x=720,y=260)
lc1 = Entry(bkd,background='honeydew')
lc1.place(x=720,y=310)
    
Button(bkd,text="Add",font='Papyrus 12 bold',fg='Yellow',bg='Black').place(x=600,y=360)
def clearall():
    book_id1.delete(0,END)
    titlee1.delete(0,END)
    autho1.delete(0,END)
    gene1.delete(0,END)
    cpy1.delete(0,END)
    lc1.delete(0,END)
    
Button(bkd,text="Clear",font='Papyrus 12 bold',fg='Yellow',bg='Black',command=lambda:clearall()).place(x=720,y=360)

bkd.mainloop()