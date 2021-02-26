import mysql.connector as sql
from tkinter import messagebox 
from tkinter import *
import csv
import time

def MainSlamPG():
    screen=Tk()
    screen.title("Slam Book -s.jana")
    screen.geometry("400x400")

    FN=StringVar()
    LN=StringVar()
    SEX=StringVar()
    RS=StringVar()
    PN=IntVar()

    def put():
        datafrom=sql.connect(host="localhost",passwd="jana1234",user="root",database="school")

        a=FN.get()
        b=LN.get()
        c=SEX.get()
        d=RS.get()
        e=PN.get()
        
        cc=datafrom.cursor()
        cc.execute("INSERT INTO friends values('{}','{}','{}','{}','{}');".format(a,b,c,d,e))
        datafrom.commit()
        datafrom.close()

    headpart=Label(text="My Slam Book")
    lineLL=Label(text="____________________________________________")

    headpart.pack()
    lineLL.pack()

    firstName=Label(text="First Name :")
    lastName=Label(text="Last Name :")
    gender=Label(text="SEX :")
    Relationship=Label(text="Relationship :")
    lablephoneNo=Label(text="Phone No. :")

    giveName=Entry(screen,textvariable=FN)
    givelastName=Entry(screen,textvariable=LN)
    giveGender=Entry(screen,textvariable=SEX)
    giveRelationship=Entry(screen,textvariable=RS)
    givelablephoneNo=Entry(screen,textvariable=PN)

    firstName.place(x=100,y=50)
    giveName.place(x=200,y=50)
    lastName.place(x=100,y=100)
    givelastName.place(x=200,y=100)
    gender.place(x=100,y=150)
    giveGender.place(x=200,y=150)
    Relationship.place(x=100,y=200)
    giveRelationship.place(x=200,y=200)
    lablephoneNo.place(x=100,y=250)
    givelablephoneNo.place(x=200,y=250)

    def end():
        screen.destroy()
    def nextp():
        put()
        messagebox.showinfo("Thank You","Thank You, Loaded in DataBase :-) ")
    def dataOut():
        datafrom=sql.connect(host='localhost',passwd='jana1234',user='root',database='school')
        mypoint=datafrom.cursor()
        mypoint.execute("SELECT * FROM friends;")

        printoutintxt = open("MySlamBook.csv",'a')
        mytyper = csv.writer(printoutintxt)
        for i in mypoint.fetchall():
            mytyper.writerow(list(i))

        printoutintxt.close()
        messagebox.showinfo("Thank You","Print Out has beed dun successfully \nnamed \"MySLamBook.csv\" in home Page ")

    cancelPG=Button(text="Cancel",command=end)
    nextPG=Button(text="Next->",command=nextp)
    printPG=Button(text="Print Out",command=dataOut)

    cancelPG.place(x=200,y=300)
    nextPG.place(x=260,y=300)
    printPG.place(x=320,y=300)

    screen.mainloop()

def ok():
    return True

