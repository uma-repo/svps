from flask import Flask,request , render_template
import mysql.connector

app = Flask(__name__)

@app.route("/" , methods=["POST" , "GET"])
def home():
    if request.method == 'POST':
        user = request.form['fname']
        print("name is:" +user)
        ##mysql code start
        conn = mysql.connector.connect(user='root', password='Pass@123', host='127.0.0.1', database='svps1')
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO students (studid, Name,Surname,phno,Fromyear,Toyear,Fromclass,Toclass,comments) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)")
        data = ('01', user, 'yerrapragada','9777777','1998','2000','3rd','5th','gfhkdsfuiugh')
        try:
            cursor.execute(insert_stmt, data)
            conn.commit()
        except:
            conn.rollback()
        print("Data inserted")
        conn.close()

        ##mysql code ends
    print("Text rendering:")
    return render_template("myform.html" , content = "Flask")

if __name__=="__main__":
    app.run(debug = True)
