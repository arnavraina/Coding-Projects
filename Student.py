class Student:
    #Intialization of Class
    def __init__(self, student_id, Name, Gender, Department,Book_id):
        self.student_id = student_id
        self.name = Name
        self.gender = Gender
        self.department = Department
        self.Book_id  = Book_id
    #Update Student Name
Student1=Student('20','Arnav','M','CS','10')