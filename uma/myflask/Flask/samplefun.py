from flask import *

app = Flask(__name__)
@app.route("/students",  methods=["GET"])
def students():
    print("enter firstname")
    fname = request. args. get('fname')
    print("enter surname")
    sname = request. args. get('sname')
    prstmt = "select * from students where fname = {fname} and  sname = {sname}"
    print(str(prstmt));
