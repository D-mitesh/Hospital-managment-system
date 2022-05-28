import mysql.connector as con
from reception import Yours_Reception as ys
class Yours_Patient:
    def __init__(self):
        self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
        self.pointer=self.mydb.cursor()
        self.uid=input("Enter Your Patient ID : ")
        self.pas=input("Enter Your Password : ")
        self.plogin()
    def plogin(self):
        self.show="select * from patient"
        self.pointer.execute(self.show)
        self.data=self.pointer.fetchall()
        for i in self.data:
            if i[0]==self.uid:
                if i[1]==self.pas:
                    print("You are logged in!")
                    self.pfunc()
                    break
                else:
                    print("You've entered incorrect password!Please enter correct password")
                    self.__init__()
                break
        else:
            print("You are not here or entered wrong userid!Please contact receptionist for registeration or enter correct user id")
            self.__init__()
    def pfunc(self):
        choice=int(input("1:See Your Details,2:Update your details"))
        if choice==1:
            ys.patient_sec.patient_show(self.uid)
        elif choice==2:
            self.pupdt()
        else:
            print("No such option available!")
            self.pfunc()
    def pupdt(self):
        print("Enter 1 for Password")
        print("Enter 2 for Name")
        print("Enter 3 for Address")
        print("Enter 4 for Mobile Number")
        print("Enter 5 for Relative's Name")
        print("Enter 6 for Relative's Relation")
        chnge=int(input("What you want to update : "))
        if chnge==1:
            old=input("Enter Your old password : ")
            if old==self.pas:
                nchnge=input("Create new password containing atleast one uppercase,one lowercase,one punctuation symbol,one digit : ")
            else:
                print("Entered password is incorrect!Please enter correct one")
            query=("update patient set password=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==2:
            nchnge=input("Enter Name to change : ").lower()
            query=("update patient set patient_name=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==3:
            nchnge=input("Change Address : ")
            query=("update patient set address=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==4:
            nchnge=input("Change Moble Number : ")
            query=("update patient set Mobile_number=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==5:
            nchnge=input("Change relative's name : ")
            query=("update patient set relative_name=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        elif chnge==6:
            nchnge=input("Change relative's relation : ")
            query=("update patient set relative_relation=%s where patient_id=%s")
            self.pointer.execute(query,(nchnge,self.uid,))
            self.mydb.commit()
            print("Changes saved!")
        else:
            print("No such option available!")
            self.pupdt()