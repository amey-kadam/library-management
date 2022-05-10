from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from typing import Sized 
from PIL import Image,ImageTk
import random
import sqlite3 


sb = Tk()
sb.geometry('1400x1400')
sb.state('zoomed')
sb.configure(background="black")

c4=Canvas(sb,bg="black",width=460,height=380)
c4.place(x=450,y=50)

ent = Entry(sb,bg="white")
ent.place(x=480,y=130,width=100,height=220)
ent2 = Entry(sb,bg="white")
ent2.place(x=580,y=130,width=100,height=220)
ent3 = Entry(sb,bg="white")
ent3.place(x=680,y=130,width=100,height=220)
ent4 = Entry(sb,bg="white")
ent4.place(x=780,y=130,width=100,height=220)


Label(sb, text="Book id",width=13,font='Papyrus 12',fg='Yellow',bg='Black').place(x=460,y=100)

Label(sb, text="Student id",width=12,font='Papyrus 12',fg='Yellow',bg='Black').place(x=565,y=100)

Label(sb, text="issue date",width=7,font='Papyrus 12',fg='Yellow',bg='Black').place(x=690,y=100)

Label(sb, text="return date",width=11,font='Papyrus 12',fg='Yellow',bg='Black').place(x=767,y=100)

Label(sb,text="Book/Student ID :",font='Arial 12',fg='Yellow',bg='Black').place(x=490,y=70)


Button(sb,text="Issue Date",font='Papyrus 22 ',fg='Yellow',bg='Black').place(x=50,y=50)

Button(sb,text="Return Book",font='Papyrus 22 ',fg='Yellow',bg='Black').place(x=50, y=150)

Button(sb,text="Student Activity",font='Papyrus 22 ',fg='Yellow',bg='Black').place(x=50,y=250)

Button(sb,text="Main Menu",font='Papyrus 22 ',fg='Yellow',bg='Black').place(x=50,y=350)

Button(sb,text="BACK",font='Papyrus 12',fg='Yellow',bg='Black').place(x=735,y=365)

Button(sb, text="Search",font='Papyrus 12',fg='Yellow',bg='Black').place(x=545,y=365)

entryup = Entry(sb)
entryup.place(x=757,y=70)


sb.mainloop()