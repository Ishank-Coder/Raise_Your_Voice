import time
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask import Flask, session, request, render_template,redirect
from icecream import ic
from datetime import datetime
from dataEntry import process_form,popup
from dataDisplay import display, displaypopup
import dataEntry
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from flask import session
import psycopg2
import api_gateway

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/clint'

db_host = os.getenv("DATABASE_HOST")
db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USERNAME")
db_port = os.getenv("DATABASE_PORT")
db_pwd =  os.getenv("DATABASE_PASSWORD")
connection = psycopg2.connect(host = db_host, dbname = db_name, user = db_user, password = db_pwd, port = db_port)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template( "home.html")

def current_milli_time():
    return round(time.time() * 1000)


@app.route("/requestRegister.html",methods=["GET", "POST"])
def registerReq():
    
    return render_template("requestRegister.html")
@app.route('/process_formty', methods=['POST'])
def process_formty():
    start = current_milli_time()
    ok = api_gateway.create(request,connection)
    elapsed = current_milli_time() - start
    print(elapsed)
    
    if(ok):
        print("oh yeah")
        return redirect(url_for("home"))
    else:
        print("koina")
        return redirect(url_for("home"))
  

@app.route("/login", methods = ["POST"])
def login():
    return redirect(url_for("grievances"))
    

@app.route("/grievances", methods = ["GET","POST"])
def grievances():
    grlist = api_gateway.display(connection)
    
    return render_template("grievancelist.html",grlist= grlist)
    
    
@app.route("/logout", methods = ["GET","POST"])
def logout():
    return redirect(url_for("home"))

@app.route("/details/<name>", methods = ["GET"])
def details(name):
    print(name)
    dets=api_gateway.details_disp(connection,name)
    return render_template("action.html",dets = dets)
    # return redirect(url_for("actioncenter"))

# @app.route("/actioncenter", methods=["GET"])
# def actioncenter():
    
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

# @app.route("/grievancelist.html",methods=["GET", "POST"])
# def grievancelist():
#     new,pending,closed = displaypopup(request, db)
#     return render_template("grievancelist.html",new=new,pending=pending,closed=closed)


# cred = credentials.Certificate('static//grievance-2ba24-firebase-adminsdk-kg434-599944587c.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/',
#     'storageBucket': 'grievance-2ba24.appspot.com'
# })



# @app.route('/process_formty', methods=['POST'])
# def process_formty():
    
#     process_form(request,db,storage)
#     return redirect(url_for("home"))  # Make sure you have a return statement here



# @app.route('/actiontaken', methods=['POST'])
# def att():
#     daa = get_session('pdata')
#     dataEntry.at(request,db,daa)
#     return redirect(url_for('popsup'))


# @app.route('/popup', methods=["GET",'POST'])
# def popsup():
#     newji,username=popup(request,db)
             
#     new,pending,closed,data = displaypopup(newji,db)
#     flag_new,flag_pend,flag_closed= True,True,True
#     if len(new)==0:
#         flag_new = False
#     if len(pending)==0:
#         flag_pend = False
#     if len(closed)==0:
#         flag_closed = False
#     set_session("username",username)
#     set_session("data",data)
#     ic(data)
    
#     return render_template("grievancelist.html",new=new,pending=pending,closed=closed,flag_new=flag_new,flag_pend=flag_pend,flag_closed=flag_closed,data=data)
#     # return render_template("grievancelist.html",new=newji)

# @app.route('/action.html/<name>', methods=["GET",'POST'])
# def details(name):
#     set_session('name',name)
    
#     gid = name[1]
#     data = get_session('data')
#     ic(data)
#     set_session('pdata',data)
#     username = get_session('username')
   
#     to=display(db,name,data,username)
#     # print(to)
#     # set_session('to',to)
#     return render_template("action.html",toll=to)
#     # form = UploadFileForm()

#     # return redirect(url_for('action'))
#     # return render_template("action.html")



# @app.route("/admindetail.html",methods=["GET", "POST"])
# def admindetail():
#     return render_template("admindetail.html")

# @app.route("/adminpanel.html",methods=["GET", "POST"])
# def adminpanel():
#     return render_template("adminpanel.html")

# @app.route('/logout')
# def logout():

#     session.clear()
#     return redirect(url_for('home'))

# def set_session(key,value):
#     session[key] = value  # Set a session variable
    

# def get_session(key):
#     # username = session.get('username')  # Get a session variable
#     return session.get(key)

# # @app.route("")
# # def taking():
# #     to=display(db)
# #     form = UploadFileForm()

# #     return render_template('action.html',to = to, form=form)

if __name__ == '__main__':
    app.run()


