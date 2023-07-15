def display(db):
    
    ref = db.reference()
    data = ref.child("ConvenerRelatedGrievance").child("Exam").child("07060078507").child("StudentGrievance").get()
    print(data)
    return(data)
    # todo = db.child("todo").get()
    # to = todo.val()
    # return(to)

def displaypopup(db):
    
    ref = db.reference('ConvenerRelatedGrievance/Exam')
    data = ref.get()
    print(data)
    news = []
    pend=[]
    close = []
    for key, value in data.items():
        if 'status' in value.get('StudentGrievance', {}):
            if value['StudentGrievance']['status'] == 'new':
                news.append(value['StudentGrievance']['name'])
            elif value['StudentGrievance']['status'] == 'pending':
                pend.append(value['StudentGrievance']['name'])
            else:
                close.append(value['StudentGrievance']['name'])

    return(news)