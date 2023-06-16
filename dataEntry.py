def process_form(request,db):
    from flask import Flask, redirect, render_template, url_for 
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
    send_data(tog,data,db)
    
    
def send_data(tog,data,db):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'
    abc = "todoto"
    ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)