from flask import Flask, redirect, render_template, url_for
from flask import Flask, session, request, render_template,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dataEntry import process_form
from dataDisplay import display
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import getDatalist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

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
    return render_template("requestRegister.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/grievancelist.html",methods=["GET", "POST"])
def grievancelist():
    new,pending,closed = getDatalist.getlist(request, db)
    
    
    
    return render_template("grievancelist.html",new=new,pending=pending,closed=closed)

@app.route("/action.html",methods=["GET", "POST"])
def taking():
    to=display(db)
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('action.html',to = to, form=form)


cred = credentials.Certificate('static//grievance-2ba24-firebase-adminsdk-kg434-599944587c.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/'
})

@app.route('/process_form', methods=['POST'])
def process_formrty():
    process_form(request,db)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()


