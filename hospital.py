import mysql.connector as con
from patient import Yours_Patient
from staff import Yours_Staff
class Yours_Hospital:
    def __init__(self):
        self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
        print("<<<<Welcome to YOURS HOSPITAL>>>>")
        self.pointer=self.mydb.cursor()
        self.user=str(input("1:Patient , 2:Staff >>>")).lower()
        if self.user=="1":
            pobj=Yours_Patient
            pobj()
        elif self.user=="2":
            sobj=Yours_Staff
            sobj()
        else:
            print("Wrong Option entered!")
            self.__init__()
hos=Yours_Hospital
hos()