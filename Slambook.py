import mysql.connector as sql
from tkinter import messagebox 
from tkinter import *
import time

screen=Tk()
screen.title("Slam Book -js")
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

headpart=Label(text="My Slam Book")
lineLL=Label(text="____________________________________________")

headpart.pack()
lineLL.pack()

firstName=Label(text="First Name :")
lastName=Label(text="Last Name :")
l5=Label(text="SEX :")
l6=Label(text="Relationship :")
l7=Label(text="Phone No. :")

giveName=Entry(screen,textvariable=FN)
givelastName=Entry(screen,textvariable=LN)
e3=Entry(screen,textvariable=SEX)
e4=Entry(screen,textvariable=RS)
e5=Entry(screen,textvariable=PN)

firstName.place(x=100,y=50)
giveName.place(x=200,y=50)
lastName.place(x=100,y=100)
givelastName.place(x=200,y=100)
l5.place(x=100,y=150)
e3.place(x=200,y=150)
l6.place(x=100,y=200)
e4.place(x=200,y=200)
l7.place(x=100,y=250)
e5.place(x=200,y=250)

def end():
    screen.destroy()
def nextp():
    put()
    messagebox.showinfo("Thank You","Thank You, Loaded in DataBase :-) ")
def dataOut():
    pass

cancelPG=Button(text="Cancel",command=end)
nextPG=Button(text="Next->",command=nextp)
printPG=Button(text="Print Out",command=dataOut)

cancelPG.place(x=300,y=300)
nextPG.place(x=400,y=300)
printPG.place(x=400,y=300)

screen.mainloop()

def ok():
    return True

