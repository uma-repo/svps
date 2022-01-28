import mysql.connector

#establishing the connection
conn = mysql.connector.connect(9user='root', password='Pass@123', host='127.0.0.1', database='svps')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO students (studid, Name,Surname,phno,Fromyear,Toyear,Fromclass,Toclass,comments)"
   "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)"
)
data = ('01', 'uma', 'yerrapragada','9777777','1998','2000','3rd','5th','gfhkdsfuiugh')

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()