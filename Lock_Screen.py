from tkinter import *
from tkinter import messagebox
import Verification as MyOTP
import mysql.connector as mysql
import Slambook as myBook

GetOTP=None
move=None
screen = Tk()
screen1 = Tk()
screen2 = Tk()

connection = mysql.connect(user='mysql', password='jana1234', host='localhost', database='mysql')

def checkLogin(username,password):
    checker = connection.cursor()
    checker.execute("SELECT * FROM loginData;")
    data = checker.fetchall()
    if([username,password] in data):
        messagebox.showinfo("Last step","Great Your account is exsisting\nSo, Now enter your Phone No. For OTP")
    else:
        messagebox.showwarning("Sorry","Something went wrong\nPlease check your details or you might not have account!")

def signupDataIn(username,password,phoneNoForNew):
    checker = connection.cursor()
    checker.execute("INSERT INTO loginData values('{}','{}','{}');".format(username,password,phoneNoForNew))
    connection.commit()
    messagebox.showinfo("Great","Your Account has successfully created")


def lockscreen(stay):   
    screen.geometry("200x40")
    if(stay==True):       
        screen.configure(background='black')
        screen.title("Lock Screen")
        login = Button(screen,text="Login")
        signup = Button(screen,text="Signup")
        login.place(x=55, y=8)
        signup.place(x=105, y=8)
        screen.mainloop()
    else:
        screen.destroy()

def giveMeOTP():
    global GetOTP
    phoneNO=myOTPV.get()
    print("yea sended OTP to no.",str(phoneNO))
    GetOTP = MyOTP.generateOTP(phoneNO)
    print(GetOTP)

def userOTP():
    global move
    if(str(GetOTP)==str(enterYOTP.get())):
        screen1.destroy()
    else:
        messagebox.showwarning("Wrong OTP","the OTP which you have given is wrong")

def loginPage(stay):
    global myOTPV,enterYOTP,screen
    
    screen1.geometry("400x400")
    if(stay==True):
        screen1.title("Login")
        myOTPV=Entry(screen1)
        myOTPV.place(x=50,y=300)
        sendOTP = Button(screen1,text="Send OTP",command = giveMeOTP)
        sendOTP.place(x=240,y=297)
        

        enterYOTP=Entry(screen1)
        enterYOTP.place(x=100,y=350)

        nextPG = Button(screen1,text="Next",command = userOTP)
        nextPG.place(x=310,y=350)

        screen1.mainloop()      
    else:
        screen1.destroy()

loginPage(True)
def ok():
    return True
