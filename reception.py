from configparser import DuplicateSectionError
import mysql.connector as con
from mysql.connector.abstracts import DUPLICATED_IN_LIST_ERROR as duperror
from pssgen import generation
class Yours_Reception:
    def __init__(self):
        self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
        print("<<<<Welcome>>>>")
        self.pointer=self.mydb.cursor()
        opt=str(input("1:PATIENT SECTION,2:STAFF SECTION>>>")).lower()
        if opt=="1":
            patsec=self.patient_sec
            patsec()
        elif opt=="2":
            staffsec=self.staff_sec
            staffsec()
        else:
            print("No such option available!")
            self.__init__()
    class patient_sec:
        def __init__(self):
            self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
            self.pointer=self.mydb.cursor()
            opt=int(input("1:Patient Entry,2:See Patient details,3:Update details or Discharge(delete data) =>"))
            if opt==1:
                self.patient_reg()
            elif opt==2:
                self.pid=input("Please Enter Patient ID : ")
                self.patient_show(self.pid)
            elif opt==3:
                self.pid=input("Please Enter Patient ID : ")
                self.patient_update(self.pid)
            else:
                print("No such option available!Please enter correct option.")
                self.__init__()
        def patient_reg(self):
            try:
                print("<<<<PATIENT REGISTRATION FORM>>>>")
                print("Please enter below information correctly.")
                name=input("Enter patient name : ").lower()
                add=input("Enter patient's address : ")
                mobno=int((input("Enter Mobile Number : ")))
                relname=input("Enter patient one relative's name : ").capitalize()
                relrela=input("Enter relative's relation with patient : ")
                prob=input("Enter patient's health problem : ")
                indate=input("Enter Patient-in date[YYYY\MM\DD] : ")
                self.pid=generation.userid()
                self.ppass=generation.password()
                deta=(self.pid,self.ppass,name,add,mobno,relname,relrela,prob,indate)
                ins="insert into patient(patient_id,password,patient_name,address,Mobile_number,relative_name,relative_relation,health_problem,patient_in) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                self.pointer.execute(ins,deta)
                self.mydb.commit()
                print("Patient registered successfully!")
                print(" Patient User ID : ",self.pid)
                print(" Patient Password : ",self.ppass)
                self.mydb.close()
                self.__init__()
            except Exception as error:
                print("Error occured : ",error)
                self.__init__()
        def patient_show(self,pid):
            self.show="select * from patient"
            self.pointer.execute(self.show)
            self.data=self.pointer.fetchall()
            for i in self.data:
                if i[0]==self.pid:
                    print("Patient ID : ",i[0])
                    print("Patient name : ",i[2])
                    print("Patient's address : ",i[3])
                    print("Mobile Number : ",i[4])
                    print("Relative's name : ",i[5])
                    print("Relative's relation with patient : ",i[6])
                    print("Patient's health problem : ",i[7])
                    print("Admit date : ",i[8])
                    print("Name of doctor alloted for patient : ",i[9])
                    print("Bed no.,Ward no. \ Room no. : ",i[10])
                    print("Patient-in : ",i[11])
                    print("Patient-out : ",i[12])
                    break
            else:
                print("Data not available!")
                self.__init__()
        def patient_update(self,pid):
            print("Enter 1 for Name")
            print("Enter 2 for Address")
            print("Enter 3 for Mobile Number")
            print("Enter 4 for Relative's Name")
            print("Enter 5 for Relative's Relation")
            print("Enter 6 for Health problem")
            print("Enter 7 for Admit date")
            print("Enter 8 for Name of Doctor")
            print("Enter 9 for Bed no.,Ward no. \ Room no.")
            print("Enter 10 for Patient-in")
            print("Enter 11 for Patient-out")
            print("Enter 12 to delete patient record")
            chnge=int(input("Enter Your option : "))
            if chnge==1:
                nchnge=input("Enter Name to change : ").lower()
                query=("update patient set patient_name=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==2:
                nchnge=input("Change Address : ")
                query=("update patient set address=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==3:
                nchnge=input("Change Moble Number : ")
                query=("update patient set Mobile_number=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==4:
                nchnge=input("Change relative's name : ")
                query=("update patient set relative_name=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==5:
                nchnge=input("Change relative's relation : ")
                query=("update patient set relative_relation=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==6:
                nchnge=input("Health Problem : ")
                query=("update patient set health_problem=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==7:
                nchnge=input("Change admit date[YYYY\MM\DD] : ")
                query=("update patient set admitted_date=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==8:
                nchnge=input("update/Change name of doctor alloted  : ")
                query=("update patient set doctor_name=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==9:
                nchnge=input("Change Bed no.,Ward no. \ Room no. : ")
                query=("update patient set room_no=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==10:
                nchnge=input("Change Patient-in[YYYY\MM\DD] : ")
                query=("update patient set patient_in=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==11:
                nchnge=input("Change Patient-out[YYYY\MM\DD] : ")
                query=("update patient set patient_out=%s where patient_id=%s")
                self.pointer.execute(query,(nchnge,self.pid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==12:
                query="delete from patient where patient_id=%s"
                self.pointer.execute(query,(self.pid,))
                self.mydb.commit()
                print("Patient data deleted!")
            else:
                print("No such option available")
                self.patient_update()
    class staff_sec:
        def __init__(self):
            self.mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
            self.pointer=self.mydb.cursor()
            opt2=int(input("1:Staff registration,2:See Staff Details,3:Update or Delete Data : "))
            if opt2==1:
                self.sreg()
            elif opt2==2:
                self.sid=input("Enter Staff ID : ")
                self.staff_show(self.sid)
            elif opt2==3:
                self.sid=input("Enter Staff ID : ")
                self.staff_update(self.sid)
            else:
                print("No such option available!Please choose correct one.")
        def sreg(self):
            try:
                self.name=input("Enter name : ").lower()
                adr=input("Enter address : ")
                mobno=int(input("Enter Mobile Number : "))
                work=input("Enter profession : ")
                officeno=input("Enter office no. if any  allotted otherwise enter 0 : ")
                join=input("Enter Joining date[YYYY\MM\DD] : ")
                sid=generation.userid()
                spass=generation.password()
                tup=(sid,spass,self.name,adr,mobno,work,officeno,join)
                ins="insert into staff(staff_id,password,staff_name,address,Mobile_number,designation,office_no,joining_date) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                self.pointer.execute(ins,tup)
                self.mydb.commit()
                print("Patient registered successfully!")
                print("User ID : ",sid)
                print("Password : ",spass)
                self.mydb.close()
                self.__init__()
            except Exception as error:
                print("Error occured : ",error)
                self.__init__()
        def staff_show(self,sid):
            self.show="select * from staff"
            self.pointer.execute(self.show)
            self.data=self.pointer.fetchall()
            for i in self.data:
                if i[0]==self.sid:
                    print("Staff ID : ",i[0])
                    print("Staff name : ",i[2])
                    print("Staff's address : ",i[3])
                    print("Mobile Number : ",i[4])
                    print("Designation : ",i[5])
                    print("Office no. : ",i[6])
                    print("Joining date : ",i[7])
                    print("Leaving date : ",i[8])
                    break
                else:
                    print("Data not available!")
                    self.__init__()
        def staff_update(self,sid):
            print("Enter 1 for Name")
            print("Enter 2 for Address")
            print("Enter 3 for Mobile Number")
            print("Enter 4 for Designation")
            print("Enter 5 for Office no.")
            print("Enter 6 for Joining date")
            print("Enter 7 for leaving date")
            print("Enter  for data deletion")
            chnge=int(input("What you want to change : "))
            if chnge==1:
                nchnge=input("Enter Name to change : ").lower()
                query=("update staff set staff_name=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==2:
                nchnge=input("Change Address : ")
                query=("update staff set address=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==3:
                nchnge=input("Change Moble Number : ")
                query=("update staff set Mobile_number=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==4:
                nchnge=input("Change Designation : ")
                query=("update staff set designation=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==5:
                nchnge=input("Change Office no : ")
                query=("update staff set office_no=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==6:
                nchnge=input("Health Problem[YYYY\MM\DD] : ")
                query=("update staff set joining_date=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==7:
                nchnge=input("Change leaving date[YYYY\MM\DD] : ")
                query=("update staff set leaving_date=%s where staff_id=%s")
                self.pointer.execute(query,(nchnge,self.sid,))
                self.mydb.commit()
                print("Changes saved!")
            elif chnge==8:
                query="delete from staff where staff_id=%s"
                self.pointer.execute(query,(self.sid,))
                self.mydb.commit()
                print("Staff data deleted!")
            else:
                print("No such option available")
                self.staff_update()