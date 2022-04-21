from flask import Flask,request , render_template

app = Flask(__name__)

@app.route("/" , methods=["POST" , "GET"])
def home():
    if request.method == 'POST':
        user = request.form['fname']
        print("name is:" +user)
        ##mysql code start

        ##mysql code ends
    print("Text rendering:")
    return render_template("myform.html" , content = "Flask")

if __name__=="__main__":
    app.run(debug = True)