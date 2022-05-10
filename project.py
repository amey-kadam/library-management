from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from typing import Sized
import tkinter as tk 
from PIL import Image,ImageTk
import random
import sqlite3

def showhomescreen():
    
    root = Tk()
    root.title("home screen")
    root.geometry('1280x1920')
    root.state('zoomed')
    
    bg=tk.PhotoImage(file="C:\\Users\\ameyp\\Downloads\\download2.png")

    canvas1 = Canvas( root, width = 400, height = 400)
    
    canvas1.pack(fill ="both", expand = True)
    
    # Display image
    canvas1.create_image( 20, 20, image = img,  anchor = "NW")
        
    #root.configure(bg)   

    Label(root, text="Welcome",font=("Brush Script MT",40),bg="black",fg="#228B22").place(x=440,y=165)
    Label(root, text="to",font=("Brush Script MT",40),bg="black",fg="white").place(x=595,y=165)
    Label(root, text="great",font=("Brush Script MT",40),bg="black",fg="#228B22").place(x=640,y=165)
    Label(root, text="Library",font=("Brush Script MT",40),bg="black",fg="white").place(x=740,y=165)
    
    Button(root,text="BOOK DATA",font=("Brush Script MT",25),bg="black",fg="orange").place(x=330,y=436)

    Button(root,text="STUDENT DATA",font=("Brush Script MT",25),bg="black",fg="orange").place(x=750,y=436)
    
    bg=PhotoImage(file="C:\\Users\\ameyp\\Downloads\\download2.png")
    
   

    root.mainloop()
    

if __name__ == "__main__":
    win=Tk()
    win.geometry('1280x1920')
win.state('zoomed')


C1=Canvas(win,width=1280,height=1920)
C1.pack()
image=Image.open("C:\\Users\\ameyp\\Downloads\\download1.png")
#resize_image = image.resize((1400,700))
img=ImageTk.PhotoImage(image)
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


lgn  =Button(win,text="Login",font=("Brush Script MT",20),bg="black",fg="#FF9912",command=showhomescreen)
lgn.place(x=600,y=380)

 
win.mainloop() 
