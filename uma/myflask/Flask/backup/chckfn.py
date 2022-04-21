import mysql.connector
def getAllStudents():
    conn = mysql.connector.connect(user='root', password='Pass@123', host='127.0.0.1', database='svps1')
    cursor = conn.cursor()
    print("getting all students details")
    stmt = "select Name , Surname ,Phno from students "
    print(stmt)
    cursor.execute(stmt)
    studetails = cursor.fetchall()
    print("details: " +str(studetails))

    for detail in studetails:
        print(detail)

getAllStudents()

