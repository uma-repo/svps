from distutils.log import error
from flask import *
import mysql.connector

app = Flask(__name__)
@app.route("/",  methods=["GET" , "POST"])
def form():
    print("rendering home")
    return render_template("regform.html" , content = "Flask")

   

@app.route("/add_data" , methods=["GET" , "POST"])

def add_data():
    print("test1")
    print(request.method)
    
    if request.method == 'POST':
        print("check")
        print(request.form)
        user = request.form['fname']
        suname = request.form['sname']
        print("name is:" +user)
        print("surname is:"+suname)
        pno = request.form['phno']
        print("phno is:"+pno)
        fmyear = request.form['fyear']
        toyear = request.form['tyear']
        fclas = request.form['fclas']
        tclas = request.form['tclas']
        cmt = request.form['comment']
        ##mysql code start
        conn = mysql.connector.connect(user='root', password='Pass@123', host='127.0.0.1', database='svps1')
        cursor = conn.cursor()
        insert_stmt = ("INSERT INTO students (studid, Name,Surname,phno,Fromyear,Toyear,Fromclass,Toclass,comments) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)")
        data = ('01', user, suname,pno,fmyear,toyear,fclas,tclas,cmt)
        try:
           # cursor.execute(insert_stmt, data)
           #conn.commit()
            c =  gtstdnt(user,suname)
            msg_var = "unable to register!please try later "
            print(c)
            if (len(c)>0):
                msg_var = "successfully registerd1"
                print(msg_var)
            else:
                print(msg_var)
    

            
        except Exception as e : 
            print("exception occured")
            print(str(e))
            conn.rollback()
        print("Data inserted") 
        conn.close()
          ##mysql code ends
    print("Text rendering:"+msg_var)
    return msg_var

def gtstdnt(fname,sname):
    conn = mysql.connector.connect(user='root', password='Pass@123', host='127.0.0.1', database='svps1')
    cursor = conn.cursor()
    print("checking cursor")
    stmt = "select * from  students where Name = '" + fname + "' and Surname = '" + sname +"'"
    print(stmt)
    cursor.execute(stmt)
    print("executed sueccessfully")
    # gets the number of rows affected by the command executed
    ret_rows = cursor.fetchall()
    print ("number of affected rows: " + str(len(ret_rows)))
    if ret_rows == 0:
        print ("It Does Not Exist")
        print("check return1")
    return ret_rows


              
@app.route("/transactions",  methods=["POST" , "GET"])
def transactions():
    msg = ""
    if request.method == 'POST':
        print('req method is post')
        msg = add_data()
        #msg="sec"
    return render_template("transactions-hoverinput.html" , reg_msg = msg)


if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug = True)
