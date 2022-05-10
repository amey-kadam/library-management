from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from typing import Sized 
from PIL import Image,ImageTk
import random
import sqlite3

if __name__ == "__main__":
    win=Tk()
    win.geometry('1280x1920')
win.state('zoomed')


C1=Canvas(win,width=1280,height=1920)
C1.pack()
image=Image.open("C:\\Users\\ameyp\\Downloads\\download1.png")
resize_image = image.resize((1400,700))
img=ImageTk.PhotoImage(resize_image)
C1.create_image(0,0,anchor=NW,image=img)


win.title('library managment')


admn = Label(win,text="Admin Login", font=("Brush Script MT",55),bg="black",fg="#FF9912")
admn.place(x=480,y=100)
usr = Label(win,text="Username",font=("Brush Script MT",25),bg="black",fg="#FF9912")
usr.place(x=440, y=250)
psd = Label(win,text="Password",font=("Brush Script MT",25),bg="black",fg="#FF9912")
psd.place(x=440,y=300)


admn1 = Entry(win,bg="black",fg="white")
admn1.place(x=640,y=250,width=200,height=36)
usr1 = Entry(win,bg="black",fg="white",show="*")
usr1.place(x=640,y=300,width=200,height=36)


lgn  =Button(win,text="Login",font=("Brush Script MT",20),bg="black",fg="#FF9912")
lgn.place(x=600,y=380)
win.mainloop() 