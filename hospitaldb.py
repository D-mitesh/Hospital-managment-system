import mysql.connector as con
from mysql.connector.errorcode import CR_COMMANDS_OUT_OF_SYNC
try:
    mydb=con.connect(host="localhost",user="root",password="0404",database="Hospital")
    print("Connection successful!")
    pointer=mydb.cursor()
    query=""
    pointer.execute(query)
    mydb.commit()
    print("Success!")
except Exception as error:
    print("Error : ",error)