from flask import Flask, redirect, render_template, url_for
from flask import Flask, session, request, render_template,redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dataEntry import process_form,popup
from dataDisplay import display, displaypopup
import dataEntry
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import getDatalist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/clint'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template( "home.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello{name}"

@app.route("/requestRegister.html",methods=["GET", "POST"])
def registerReq():
    print(3434)
    return render_template("requestRegister.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/grievancelist.html",methods=["GET", "POST"])
def grievancelist():
    new,pending,closed = displaypopup(request, db)
    return render_template("grievancelist.html",new=new,pending=pending,closed=closed)



# @app.route("/upload",methods=["GET","POST"])

# def upload_file():
#     process_form(request,db)
#     if 'file' in request.files:
#         file = request.files['file']
#         filename = secure_filename(file.filename)
#         # secure_filename = secure_filename(file.filename)
#         # Here you should save the file
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    
#     return redirect(url_for("home"))
# def taking():
#     to=display(db)
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data # First grab the file
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
#         return "File has been uploaded."
#     return render_template('action.html',to = to, form=form)


cred = credentials.Certificate('static//grievance-2ba24-firebase-adminsdk-kg434-599944587c.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/'
})

@app.route('/process_formty', methods=['POST'])
def process_formty():
    
    print("yha toh aaya1")
    # process_form(request,db)
    # print("yha toh aaya")
    # return redirect(url_for("home"))


@app.route('/actiontaken', methods=['POST'])
def att():
    dataEntry.at(request,db)
    return redirect(url_for('popsup'))


@app.route('/popup', methods=["GET",'POST'])
def popsup():
    newji=popup(request,db)
    new,pending,closed = displaypopup(db)
    flag_new,flag_pend,flag_closed= True,True,True
    if len(new)==0:
        flag_new = False
    if len(pending)==0:
        flag_pend = False
    if len(closed)==0:
        flag_closed = False
    print(flag_closed,flag_new,flag_pend)
    return render_template("grievancelist.html",new=new,pending=pending,closed=closed,flag_new=flag_new,flag_pend=flag_pend,flag_closed=flag_closed)
    # return render_template("grievancelist.html",new=newji)

# @app.route('/detail', methods=["GET",'POST'])
# def details():
    
#     return render_template("action.html")


@app.route("/admindetail.html",methods=["GET", "POST"])
def admindetail():
    return render_template("admindetail.html")

@app.route("/adminpanel.html",methods=["GET", "POST"])
def adminpanel():
    return render_template("adminpanel.html")

if __name__ == '__main__':
    app.run()


