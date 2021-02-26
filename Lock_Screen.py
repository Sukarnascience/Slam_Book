from tkinter import *
from tkinter import messagebox
import Verification as MyOTP
import mysql.connector as sql

def GatewayPage():

    UN=StringVar()
    PS=StringVar()
    PN=IntVar()
    def signup():
        datafrom=sql.connect(host="localhost",passwd="jana1234",user="root",database="school")

        a=UN.get()
        b=PS.get()
        c=PN.get()
        
        cc=datafrom.cursor()
        cc.execute("INSERT INTO account values('{}','{}','{}');".format(a,b,c))
        datafrom.commit()
        datafrom.close()

    UUN=StringVar()
    PSW=StringVar()
    def login():
        datafrom=sql.connect(host="localhost",passwd="jana1234",user="root",database="school")

        a=UUN.get()
        b=PSW.get()
        
        cc=datafrom.cursor()
        cc.execute("select * from account where username='{}' and password='{}';".format(a,b))
        data = cc.fetchall()
        if(data):
            pass
        else:
            pass

    

def ok():
    return True

