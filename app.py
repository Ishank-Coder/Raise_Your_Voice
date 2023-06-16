from flask import Flask, redirect, render_template, url_for
from flask import Flask, session, request, render_template,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dataEntry import process_form
from dataDisplay import display

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template( "home.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello{name}"

@app.route("/requestRegister.html",methods=["GET", "POST"])
def registerReq():
    return render_template("requestRegister.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/action.html",methods=["GET", "POST"])
def taking():
    to=display(db)

    return render_template('action.html',t=to.values())



cred = credentials.Certificate('assets//grievance-2ba24-firebase-adminsdk-kg434-19e2ca69b9.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/'
})

@app.route('/process_form', methods=['POST'])
def process_formrty():
    process_form(request,db)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()


