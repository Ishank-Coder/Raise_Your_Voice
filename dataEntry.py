def process_form(request,db):
    from flask import Flask, redirect, render_template, url_for 
    name = request.form.get('Name')
    email = request.form.get('Mail')
    number = request.form.get('Number')
    sem = request.form.get('Semester')
    branch = request.form.get('Branch')
    tog = request.form.get('Detail')
    Rollno = request.form.get('RollNo')
    gender = request.form.get('Gender')
    who = request.form.get('Type')
    
    data = {"name": name,"gender" : gender,"email": email,"num": number,"sem": sem,"branch": branch,"RollNo":Rollno ,"Type":who}
    send_data(tog,data,db)
    
    
def send_data(tog,data,db):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'
    abc = "todoto"
    ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)