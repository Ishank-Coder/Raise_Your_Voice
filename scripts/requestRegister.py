from flask import Flask, session, request, render_template,redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('assets//grievance-2ba24-firebase-adminsdk-kg434-19e2ca69b9.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://grievance-2ba24-default-rtdb.firebaseio.com/'
})

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form.get('name')
    send_data(name)
    
def send_data(name):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference('names')  # Replace with the desired location in the database
    ref.child("name").push(name)
    return 'Data sent successfully'
