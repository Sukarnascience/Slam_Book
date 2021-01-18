import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
import time

screen=Tk()

screen.title("Insert Data")
screen.geometry("500x500")

FN=StringVar()
LN=StringVar()
SEX=StringVar()
RS=StringVar()
PN=IntVar()

def put():
    datafrom=sql.connect(host='localhost',passwd='jana',user='root',database='py_project')
    
    A=FN.get()
    B=LN.get()
    C=SEX.get()
    D=RS.get()
    E=PN.get()
    
    cc=datafrom.cursor()
    cc.execute("INSERT INTO friends values(0,'{}','{}','{}','{}',{});".format(A,B,C,D,float(E)))
    datafrom.commit()
    cc.execute("select * from friends;")
    print(cc.fetchall())
    datafrom.close()

l1=Label(text="Welcome To s.jana Data")
l1.pack()
l2=Label(text="____________________________________________")
l2.pack()

l3=Label(text="First Name :")
l3.place(x=100,y=50)
e1=Entry(screen,textvariable=FN)
e1.place(x=200,y=50)

l4=Label(text="Last Name :")
l4.place(x=100,y=100)
e2=Entry(screen,textvariable=LN)
e2.place(x=200,y=100)

l5=Label(text="SEX :")
l5.place(x=100,y=150)
e3=Entry(screen,textvariable=SEX)
e3.place(x=200,y=150)

l6=Label(text="Relationship :")
l6.place(x=100,y=200)
e4=Entry(screen,textvariable=RS)
e4.place(x=200,y=200)

l7=Label(text="Phone No. :")
l7.place(x=100,y=250)
e5=Entry(screen,textvariable=PN)
e5.place(x=200,y=250)

def end():
    screen.destroy()
def nextp():
    put()
    messagebox.showinfo("Thank You","Thank You, Loaded in DataBase :-) ")


b1=Button(text="Cancel",command=end)
b1.place(x=300,y=300)
b2=Button(text="Next->",command=nextp)
b2.place(x=400,y=300)
screen.mainloop()

def ok():
    return True