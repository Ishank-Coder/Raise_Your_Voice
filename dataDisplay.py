def display(db):
    
    ref = db.reference()
    data = ref.child("ConvenerRelatedGrievance").child("Exam").child("07060078507").child("StudentGrievance").get()
    print(data)
    return(data)
    # todo = db.child("todo").get()
    # to = todo.val()
    # return(to)