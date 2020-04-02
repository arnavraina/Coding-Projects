class Book_id:
    #Intialization of Class
    def __init__(self, book_id, Name, author, department, student_id):
        self.book_id = book_id
        self.name = Name
        self.author = author
        self.department = department
        self.studentid = student_id

    #To Find student id,Book_id against a BookName
    def getStudent_id():
        Book_name=input("Enter Book_name")
        c.execute('SELECT Student_id,Book_id FROM Books WHERE Book_name = ?',(Book_name,))
        data=c.fetchall()
        for row in data:
            print(row)
    

