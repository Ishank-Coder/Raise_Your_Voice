def process_form(request,db):
    from flask import Flask, redirect, render_template, url_for 
    orgname = request.form.get('orgname')
    typegr = request.form.get('typegr')
    category = request.form.get('category')
    name = request.form.get('Name')
    
    #facutly details
    desig = request.form.get('Desig')
    dept = request.form.get('dept')
    mail = request.form.get('Mail')
    phnumber = request.form.get('phnumber')
    
    #student details
    year = request.form.get('year')
    branch = request.form.get('Branch')
    email = request.form.get('email')
    phno = request.form.get('phno')
    
    detailedgr=request.form.get('grievance')
    details=request.form.get('details')
    
    # tog = request.form.get('Detail')
    # Rollno = request.form.get('RollNo')
    # gender = request.form.get('Gender')
    # who = request.form.get('nickName')
    status = "new"
    datastu = {"name":name,"year":year,"branch":branch,"email":email,"Phoneno":phno,"detailedgr":detailedgr,"more":details,"status":status}
    datafac = {"name":name,"designation":desig,"Department":dept,"email":mail,"Phoneno":phnumber,"detailedgr":detailedgr,"more":details,"status":status}
    if category=="faculty":    
        send_data(typegr,datafac,db,category,phnumber) 
    else:
        send_data(typegr,datastu,db,category,phno)
    
    # data = {"name": name,"gender" : gender,"email": email,"num": number,"sem": sem,"branch": branch,"RollNo":Rollno ,"Type":who,"status":ds}
    
    # send_data(tog,data,db)




def at(request,db):
    from flask import Flask, redirect, render_template, url_for 
    name = request.form.get('action')
    email = request.form.get('status')
    
    data = {"name": name,"gender" : email}
    ref = db.reference()
    ref.child("ConvenerRelatedGrievance").child("Exam").child("7060078507").child("ActionTaking").child("Action24").set(data)


    
    
def send_data(type,data,db,category,num):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'
    print("todoto")
    ref.child("ConvenerRelatedGrievance").child(type).child(num).child(category).set(data)

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


