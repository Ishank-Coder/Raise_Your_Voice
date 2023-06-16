from flask import Flask, redirect, render_template, url_for
from flask import Flask, session, request, render_template,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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



cred = credentials.Certificate('assets//grievance-2ba24-firebase-adminsdk-kg434-19e2ca69b9.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/'
})

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form.get('name')
    email = request.form.get('email')
    number = request.form.get('num')
    sem = request.form.get('sem')
    branch = request.form.get('branch')
    tog = request.form.get('TOG')
    Rollno = request.form.get('rollno')
    gender = request.form.get('gender')
    selected_option = request.form.get('Student')
    if selected_option == 0:
        who = "Student"
    elif selected_option == 1:
        who = "Faculty"
    else:
        who = "Null"
    data = {"name": name,"gender" : gender,"email": email,"num": number,"sem": sem,"branch": branch,"RollNo":Rollno ,"Type":who}
    send_data(tog,data)
    return redirect(url_for("home"))
    
def send_data(tog,data):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'
    abc = "todoto"
    ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)

if __name__ == '__main__':
    app.run()


