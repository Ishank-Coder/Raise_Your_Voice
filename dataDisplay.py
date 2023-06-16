def display():
    todo = db.child("todo").get()
    to = todo.val()
    return(to)