from tkinter import *
from tkinter import messagebox
import Verification as MyOTP
import mysql.connector as sql
import Slambook as SLbook
import time

username = None

def GatewayPage():
    
    global username

    screen=Tk()
    screen.title("Entry Gate")
    screen.geometry("600x400")

    globalOTP = None
    def OTPsend(P_no):
        global globalOTP
        messagebox.showinfo("Regarding OTP","you have 10 second to fill the OTP")
        globalOTP = MyOTP.generateOTP(P_no)
        return globalOTP

    N_UN=StringVar()
    N_PW=StringVar()
    N_Pho=IntVar()
    VN_OTP = IntVar()
    def signup():

        global username
        global globalOTP

        datafrom=sql.connect(host="localhost",passwd="jana1234",user="root",database="school")

        Nusername=N_UN.get()
        Npasswd=N_PW.get()
        PhoneNO=N_Pho.get()
        myVVOTP=VN_OTP.get()
        if(globalOTP==myVVOTP):
            cc=datafrom.cursor()
            cc.execute("INSERT INTO account values('{}','{}','{}');".format(Nusername,Npasswd,PhoneNO))
            datafrom.commit()
            cc.execute("Create Table {} (First_Name varchar(20),Last_Name varchar(20),sex char(1),RelationShip varchar(100),PhoneNo varchar(15));".format(Nusername))
            datafrom.commit()
            username = Nusername
            datafrom.close()
        else:
            messagebox.showwarning("OTP", "The OTP which you have enter\nthat is not matching! \nSo, Please check ") 

    O_UN=StringVar()
    O_PW=StringVar()
    VY_OTP=IntVar()
    def login():

        global username
        global data

        datafrom=sql.connect(host="localhost",passwd="jana1234",user="root",database="school")

        Ousername=O_UN.get()
        Opasswd=O_PW.get()
        
        cc=datafrom.cursor()
        cc.execute("select phoneNo from account where username='{}' and password='{}';".format(Ousername,Opasswd))
        data = cc.fetchall()
        if(data):
            OTP=OTPsend(data)
            time.sleep(10)
            Verifi_its_u=VY_OTP.get()
            if(OTP==Verifi_its_u):
                username = Ousername
                screen.destroy()
                SLbook.MainSlamPG()
            else:
                messagebox.showwarning("OTP", "The OTP which you have enter\nthat is not matching! \nSo, Please check ") 
        else:
            messagebox.showerror("Error","Accoring to your details\nNO such account exist\nOr else the password might be wrong\n\nSo, Please check")
    
    l1=Label(screen,text="Login            Signup", font=("Courier",20))
    l1.pack()
    l2=Label(screen,text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", font=("Courier",20))
    l2.pack()

    l3=Label(screen,text="UserName :",font=("Courier",15))
    l3.place(x=20,y=60)
    l4=Label(screen,text="Password :",font=("Courier",15))
    l4.place(x=20,y=100)
    l5=Label(screen,text="OTP :",font=("Courier",15))
    l5.place(x=20,y=140)
    b1=Button(screen,text="Login",command=login)
    b1.place(x=130,y=200)

    u1=Entry(screen,textvariable=O_UN)
    u1.place(x=150,y=65)
    u2=Entry(screen,textvariable=O_PW)
    u2.place(x=150,y=105)
    u3=Entry(screen,textvariable=VY_OTP)
    u3.place(x=150,y=145)

    u4=Entry(screen,textvariable=N_UN)
    u4.place(x=450,y=65)
    u5=Entry(screen,textvariable=N_PW)
    u5.place(x=450,y=105)
    u6=Entry(screen,textvariable=N_Pho)
    u6.place(x=450,y=145)
    u7=Entry(screen,textvariable=VN_OTP)
    u7.place(x=450,y=225)


    l6=Label(screen,text="UserName :",font=("Courier",15))
    l6.place(x=320,y=60)
    l7=Label(screen,text="Password :",font=("Courier",15))
    l7.place(x=320,y=100)
    l8=Label(screen,text="PhoneNo. :",font=("Courier",15))
    l8.place(x=320,y=140)
    b2=Button(screen,text="Send OTP",command=OTPsend(VN_OTP.get()))
    b2.place(x=410,y=180)
    l9=Label(screen,text="OTP :",font=("Courier",15))
    l9.place(x=320,y=220)
    b3=Button(screen,text="Signup",command=signup)
    b3.place(x=415,y=280)

    screen.mainloop()

def accountName():
    global username
    return username    

def ok():
    return True
