
import time

import psycopg2.extras


CREATE_TABLE_FACULTY = (
    "CREATE TABLE IF NOT EXISTS Faculty(Faculty_ID int,Name Varchar,Designation Varchar,Grievance_Id Varchar,Department Varchar,Phone_No int,Email Varchar,Greivance TEXT, Detailed TEXT);"
)
CREATE_TABLE_STUDENTS = (
    "CREATE TABLE IF NOT EXISTS Students(Roll_Number int,Name Varchar,Branch Varchar,Grievance_Id Varchar,Year int,Phone_No int,Email Varchar,Greivance TEXT, Detailed TEXT);"
)
GET_DET_FAC = "SELECT * FROM faculty WHERE grievance_id = "
GET_DET_STU = "SELECT * FROM students WHERE grievance_id = "

INSERT_STUD = (
    "INSERT INTO Students(Roll_Number,Name,Branch,Grievance_Id,Year,Phone_No,Email,Greivance,Detailed,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
)
INSERT_FAC = (
    "INSERT INTO Faculty(Faculty_ID,Name,Designation,Grievance_Id,Department,Phone_No,Email,Greivance,Detailed,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
)

SELECT_GR_STU = "SELECT name, Grievance_ID, status FROM Students WHERE status = 'new' or status = 'pending';"
SELECT_GR_FAC = "SELECT name, Grievance_ID, status FROM Faculty WHERE status = 'new' or status = 'pending';"



def current_milli_time():
    return round(time.time() * 1000)
def create(request,connection):
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
    # ic(name1)
    Faculty_ID = request.form.get('FacultyID')
    desig = request.form.get('Desig')
    dept = request.form.get('dept')
    mail = request.form.get('Mail')
    phnumber = request.form.get('phnumber')
    
    #student details
    Roll_No = request.form.get('Roll_No')
    year = request.form.get('year')
    branch = request.form.get('Branch')
    email = request.form.get('email')
    phno = request.form.get('phno')
    
    detailedgr=request.form.get('grievance')
    details=request.form.get('details')
    # file = request.files['file']
    # tog = request.form.get('Detail')
    # Rollno = request.form.get('RollNo')
    # gender = request.form.get('Gender')
    # who = request.form.get('nickName')
    status = "new"
    # datastu = {"name":name1,'grievanceid':grievanceid,"year":year,"branch":branch,"email":email,"Phoneno":phno,"detailedgr":detailedgr,"more":details,"status":status}
    # datafac = {"name":name0,'grievanceid':grievanceid,"designation":desig,"Department":dept,"email":mail,"Phoneno":phnumber,"detailedgr":detailedgr,"more":details,"status":status}

    if category=="FacultyGrievance":    
        start = current_milli_time()
        try:
            with connection:
                with connection.cursor() as cursor:
                    # cursor.execute(CREATE_TABLE_FACULTY)
                    cursor.execute(INSERT_FAC,(Faculty_ID,name0,dept,grievanceid,desig,phnumber,mail,detailedgr,details,status))
                    connection.commit()
                    elapsed = current_milli_time() - start
                    print(elapsed)
            return(True)
        except Exception as e:
            print(e)
            return(False)
    else:
        try:
            start = current_milli_time()
            with connection:
                with connection.cursor() as cursor:
                   
                    cursor.execute(INSERT_STUD,(Roll_No,name1,branch,grievanceid,year,phno,email,detailedgr,details,status))
                    connection.commit()
                    elapsed = current_milli_time() - start
                    print(elapsed)
            return(True)
        except Exception as e:
            print(e)
            return(False)
def display(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_GR_FAC)
            fac = cursor.fetchall()
            cursor.execute(SELECT_GR_STU)
            stu = cursor.fetchall()
            data  = stu + fac
            sorted_data = sorted(data, key=lambda x: (x[2] != 'new', x[2]))
           
    return(sorted_data)

def details_disp(connection,idgr):
    
    with connection:
        with connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cursor:
            if 'St'in idgr:
                query = GET_DET_STU + "'" + idgr + "';"
            
            else:
                query = GET_DET_FAC + "'" + idgr + "';"
      
            cursor.execute(query)
            data = cursor.fetchone()
            # print(list(data.items()))
            return(dict(list(data.items())))
            # kl = dict(data[1])
            # print(kl)
            # print(data)
            
    