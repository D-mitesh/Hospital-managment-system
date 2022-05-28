import mysql.connector as con
from reception import Yours_Reception
class Yours_Staff:
    def __init__(self):
        self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
        print("<<<<Welcome>>>>")
        self.pointer=self.mydb.cursor()
        self.uid=input("Enter Your Staff ID : ")
        self.pas=input("Enter Your Password : ")
        self.slogin()
    def slogin(self):
        self.show="select * from staff"
        self.pointer.execute(self.show)
        self.data=self.pointer.fetchall()
        for i in self.data:
            if i[0]==self.uid:
                if i[1]==self.pas:
                    print("You are logged in!",self.uid)
                    if i[5]=="receptionist":#?#.(bEoc
                        obj=Yours_Reception
                        obj()
                        break
                    else:
                        print("Welcome!",self.uid)
                        self.sfunc()
                    break
                else:
                    print("You've entered incorrect password!Please enter correct password")
                    self.__init__()
                break
        else:
            print("You entered wrong user id or you are not registered!Please enter correct one or contact receptionist.")
            self.__init__()
    def sfunc(self):
        opt=int(input("1:See Data , 2:Update data : "))
        if opt==1:
            Yours_Reception.staff_sec.staff_show(self.uid)
        elif opt==2:
            self.supdt()
        else:
            print("There is no such option available!Pease choose from given.")
            self.sfunc()
    def supdt(self):
        print("Enter 1 for Password")
        print("Enter 2 for Name")
        print("Enter 3 for Address")
        print("Enter 4 for Mobile Number")
        chnge=int(input("What you want to update : "))
        if chnge==1:
            old=input("Enter Your old password : ")
            if old==self.pas:
                nchnge=input("Create new password containing atleast one uppercase,one lowercase,one punctuation symbol,one digit : ")
            else:
                print("Entered password is incorrect!Please enter correct one")
            query=("update staff set password=%s where staff_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==2:
            nchnge=input("Enter Name to change : ").lower()
            query=("update staff set staff_name=%s where staff_id=%s")
            self.pointer.execute(query,(nchnge,self.id,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==3:
            nchnge=input("Change Address : ")
            query=("update staff set address=%s where staff_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==4:
            nchnge=input("Change Moble Number : ")
            query=("update staff set Mobile_number=%s where staff_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        else:
            print("No such option available")
            self.supdt()