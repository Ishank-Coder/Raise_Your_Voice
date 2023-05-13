from flask import Flask, session, request, render_template,redirect
import pyrebase


config = {
  "apiKey": "AIzaSyBkydxJGHz5lGp4Tk7c3EeRPNWSLu_HwZM",
  "authDomain": "grievance-2ba24.firebaseapp.com",
  "databaseURL": "https://grievance-2ba24-default-rtdb.firebaseio.com",
  "projectId": "grievance-2ba24",
  "storageBucket": "grievance-2ba24.appspot.com",
  "messagingSenderId": "1064794325729",
  "appId": "1:1064794325729:web:b04525a038a415f1706da0",
  "measurementId": "G-ZJF766CKXD",
  "databaseURL": ''
    
}


firebase = pyrebase.initialize_app(config)

