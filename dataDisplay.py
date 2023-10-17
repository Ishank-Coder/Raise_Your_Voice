def display(db,nae,datas,username):
    
    ref = db.reference()
    naelist = eval(nae)
    gid = naelist[1]
    print(gid)
    # gid = 'Ex202310171552StMIET'
    matching_details = {}
    # print(datas)
    
  
    for key, value in datas.items():
        student_grievance = value.get('StudentGrievance', {})
        # print(student_grievance)
        grievance_id = student_grievance.get('grievanceid')
        # print(grievance_id)
        if str(grievance_id) == str(gid):
            print("here i am")
            matching_details=value
    
    print(matching_details)
    demnn = matching_details['StudentGrievance']
    
    
    # data = ref.child("ConvenerRelatedGrievance").child("Exam").child("07060078507").child("StudentGrievance").get()
    # print(data)
    return(demnn)
    # todo = db.child("todo").get()
    # to = todo.val()
    # return(to)

def displaypopup(tog,db):
    
    ref = db.reference(f'ConvenerRelatedGrievance/{tog}')
    data = ref.get()
    
    news = []
    
    pend=[]
    close = []
    for key, value in data.items():
        single=[]
        if 'status' in value.get('StudentGrievance', {}):
            if value['StudentGrievance']['status'] == 'new':
                single.append(value['StudentGrievance']['name'])
                single.append(value['StudentGrievance']['grievanceid'])
                news.append(single)
            elif value['StudentGrievance']['status'] == 'pending':
                single.append(value['StudentGrievance']['name'])
                single.append(value['StudentGrievance']['grievanceid'])
                pend.append(single)
            elif value['StudentGrievance']['status'] == 'resolved':
                single.append(value['StudentGrievance']['name'])
                single.append(value['StudentGrievance']['grievanceid'])
                close.append(single)
            else:
                continue

    print(data)
    return(news,pend,close,data)