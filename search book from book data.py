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

c4 = Canvas(sb,bg="black",width=560,height=380)
c4.place(x=450,y=50)
ent = Entry(sb,bg="white")
ent.place(x=480,y=100,width=100,height=220)
ent2 = Entry(sb,bg="white")
ent2.place(x=580,y=100,width=100,height=220)
ent3 = Entry(sb,bg="white")
ent3.place(x=680,y=100,width=100,height=220)
ent4 = Entry(sb,bg="white")
ent4.place(x=780,y=100,width=100,height=220)
ent5 = Entry(sb,bg="white")
ent5.place(x=880,y=100,width=100,height=220)

Button(sb,text="Add Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=50)

Button(sb,text="Search Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50, y=150)

Button(sb,text="All Books",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=250)

Button(sb,text="Main Menu",font='Papyrus 22 bold',fg='Yellow',bg='Black').place(x=50,y=350)

Button(sb,text="BACK",font='Papyrus 12',fg='Yellow',bg='Black',border=0).place(x=690,y=350)   
    
Label(sb, text="Book id",width=20).place(x=480,y=70)

Label(sb, text="title",width=12).place(x=590,y=70)

Label(sb, text="AUTHOR",width=21).place(x=660,y=70)

Label(sb, text="Gener",width=10).place(x=800,y=70)

Label(sb, text="Copies",width=15).place(x=870,y=70)

sb.mainloop()
