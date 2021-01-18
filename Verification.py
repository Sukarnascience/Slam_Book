import socket
from tkinter import messagebox
from tkinter import *
import random
import requests
import json

key = "jSMnfehztjfkQurNjzt7QByBEPlltccIDG0yfrGiZp6"

screen = Tk()
OTP=None

def ok():
    screen.geometry("200x20")
    screen.title("Error")
    dataP = Label(screen,text="No Internet Connection")
    dataP.pack()  
    while True:   
        ip=socket.gethostbyname(socket.gethostname())
        if(ip=="127.0.0.1"):
            messagebox.showwarning("Connection","Please connect to your internet,\nby which we can send you a OTP")
            continue
        else:
            break
    return True

def generateOTP(phoneNo="9113688393"):
    eventName = "give_OTP"
    ip=socket.gethostbyname(socket.gethostname())
    if(ip=="127.0.0.1"):
        OTP=0
    else:
        OTP=random.randint(10000,99999)
        myData={ "value1" : str(phoneNo), "value2" : str(OTP)}
        url = ("https://maker.ifttt.com/trigger/{}/with/key/{}").format(eventName,key)
        requests.post(
            url,data=json.dumps(myData),
            headers={'Content-Type':'application/json'}
        )
    return OTP
