from icecream import ic
def process_form(request,db,storage):
    from flask import Flask, redirect, render_template, url_for
    from datetime import datetime
    now = datetime.now()

    # Format it as 'YYYYMMDDHHMM'
    timestamp_str = now.strftime("%Y%m%d%H%M")
    # name = request.form.get('name')
   
# Get the current date and time
    orgname = request.form.get('orgname')
    typegr = request.form.get('typegr')
    category = request.form.get('category')
    grievanceid = typegr[0:2] + timestamp_str + category[0:2] + orgname[0:4]
    #facutly details
    name0 = request.form.get('Name0')
    name1 = request.form.get('Name1')
    ic(name1)
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
    file = request.files['file']
    # tog = request.form.get('Detail')
    # Rollno = request.form.get('RollNo')
    # gender = request.form.get('Gender')
    # who = request.form.get('nickName')
    status = "new"
    datastu = {"name":name1,'grievanceid':grievanceid,"year":year,"branch":branch,"email":email,"Phoneno":phno,"detailedgr":detailedgr,"more":details,"status":status}
    datafac = {"name":name0,'grievanceid':grievanceid,"designation":desig,"Department":dept,"email":mail,"Phoneno":phnumber,"detailedgr":detailedgr,"more":details,"status":status}

    if category=="FacultyGrievance":    
        send_data(typegr,datafac,db,category,phnumber,storage,file) 
    else:
        send_data(typegr,datastu,db,category,phno,storage,file)
    
    # data = {"name": name,"gender" : gender,"email": email,"num": number,"sem": sem,"branch": branch,"RollNo":Rollno ,"Type":who,"status":ds}
    
    # send_data(tog,data,db)




def at(request,db):
    from flask import Flask, redirect, render_template, url_for 
    name = request.form.get('action')
    email = request.form.get('status')
    
    data = {"name": name,"gender" : email}
    ref = db.reference()
    ref.child("ConvenerRelatedGrievance").child("Exam").child("7060078507").child("ActionTaking").child("Action24").set(data)


    
    
def send_data(type,data,db,category,num,storage,file):
    # data = request.json  # Assuming you're receiving data as JSON in the request
    ref = db.reference()
    # # Replace with the desired location in the database
    # ref.child("name").push(name)
    # return 'Data sent successfully'

    folder_path = f"{num}/"  # Assuming 'num' is the folder name

    # Construct the full file path (including the folder)
    full_file_path = folder_path + file.filename

    # Create a Blob object with the full file path
    blob = storage.bucket().blob(full_file_path)

    # Upload the file to Firebase Storage
    blob.upload_from_string(file.read(), content_type=file.content_type)

    # Add the file URL to the data
    storage_url = blob.public_url

    data['file_url'] = storage_url    


    # storage_ref = storage.bucket().blob(file.filename)
    # storage_ref.upload_from_string(file.read(), content_type=file.content_type)
    
    # folder_path = f"{num}/" 

   
    # full_file_path = folder_path + file.filename

    # # Upload the file to Firebase Storage
    # storage_ref = storage.bucket().blob(full_file_path)
    # storage_ref.upload_from_string(file.read(), content_type=file.content_type)

    # # Add the file URL to the data
    # storage_url = f"gs://{storage_ref.bucket.name}/{full_file_path}"
    # data['file_url'] = storage_url
    
    # ic(data)
    ref.child("ConvenerRelatedGrievance").child(type).child(num).child(category).set(data)

def popup(request,db):
    from dataDisplay import displaypopup
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'Exam':
        if password == 'pp':
            st = "Exam"
    elif username == 'Woman':
        if password == 'Woman_Manager_MIET':
            st = "Woman"
            
    
    # data = {"name": Username,"key" : Password}
    # st=displaypopup(db)
    return(st,username)

# def sendpopupdata(tog,data,db):
#     ref = db.reference()
#     # # Replace with the desired location in the database
#     # ref.child("name").push(name)
#     # return 'Data sent successfully'
#     abc = "todoto"
#     ref.child("ConvenerRelatedGrievance").child(tog).child(data["num"]).child("StudentGrievance").set(data)


