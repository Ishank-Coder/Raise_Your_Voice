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
    who = request.form.get('nickName')
    print(1234456)
    data = {"name": name,"gender" : gender,"email": email,"num": number,"sem": sem,"branch": branch,"RollNo":Rollno ,"Type":who}
    send_data(tog,data,db)




def at(request,db):
    from flask import Flask, redirect, render_template, url_for 
    name = request.form.get('action')
    email = request.form.get('status')
    
    data = {"name": name,"gender" : email}
    ref = db.reference()
    ref.child("ConvenerRelatedGrievance").child("Exam").child("7060078507").child("ActionTaking").child("Action24").set(data)


    
    
def send_data(tog,data,db):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'
    print("todoto")
    ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)

def popup(request,db):
    from dataDisplay import displaypopup
    Username = request.form.get('username')
    Password = request.form.get('password')
    data = {"name": Username,"key" : Password}
    st=displaypopup(db)
    return(st)

# def sendpopupdata(tog,data,db):
#     ref = db.reference()
#     # # Replace with the desired location in the database
#     # ref.child("name").push(name)
#     # return 'Data sent successfully'
#     abc = "todoto"
#     ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)


