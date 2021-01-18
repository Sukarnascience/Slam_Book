import mysql.connector as mysql

account = ""

def printout():
    dataout=open("YourData.txt",'w')
    connection = mysql.connect(user='mysql', password='jana1234', host='localhost', database='mysql')
    checker = connection.cursor()
    checker.execute("SELECT * FROM {};".format(account))
    data = checker.fetchall()
    for i in data:
        pass
    # taking break 
