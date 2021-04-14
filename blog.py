from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from functools import wraps

app = Flask(__name__)
app.secret_key= "MAEBLOG"

@app.route("/")
def mainpg():
   return render_template("main.html")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
