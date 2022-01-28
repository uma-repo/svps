from flask import Flask,request , render_template
import mysql.connector

app = Flask(__name__)
@app.route("/",  methods=["POST" , "GET"])
def form():
    print("rendering home")
    return render_template("regform.html" , content = "Flask")

@app.route("/form" , methods=["POST" , "GET"])
def home():
    print("test1")
    if request.method == 'POST':
        print("check")
        user = request.form['fname']
        print("name is:" +user)
        suname = request.form['sname']
        print("surname is:"+suname)
        pno = request.form['phno']
        print("phno is:"+pno)
        fmyear = request.form['fyear']
        toyear = request.form['tyear']
        fclas = request.form['fclas']
        tclas = request.form['tclas']
        cmt = request.form['comment']
        ##mysql code start
        conn = mysql.connector.connect(user='root', password='Pass@123', host='127.0.0.1', database='svps')
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO students (studid, Name,Surname,phno,Fromyear,Toyear,Fromclass,Toclass,comments) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)")
        data = ('01', user, suname,pno,fmyear,toyear,fclas,tclas,cmt)
        try:
            cursor.execute(insert_stmt, data)
            conn.commit()
        except:
            conn.rollback()
        print("Data inserted")
        conn.close()

        ##mysql code ends
    print("Text rendering:")
    return render_template("form.html" , content = "Flask")

if __name__=="__main__":
    app.run(debug = True)