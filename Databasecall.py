import sqlite3
from Student import Student
from Book import Book
#Student1=Student('20','Arnav','M','CS','10')

class Librarydatabase:
    #Intialising the database file

    def __init__(self, database = "Lib3.db"):
        self.database = database
        self.connect_db()

    # Connect Database to Access Rows
    def connect_db(self):
        self.connection=sqlite3.connect(self.database)
        self.cursor=self.connection.cursor()
    # For Querying Database    
    def query(self):
        query=input("Enter your query")
        try:
            #self.cursor.execute('DELETE FROM BOOKS WHERE ? = ? ',[column_name,value,])
            self.cursor.execute(query)
        except:
            print('Incorrect Query')
        output=self.cursor.fetchall()
        #rint(len(output))
        for data in output:
            print(data)
        if output == []:
            print("Wrong values fetched in query")
        self.connection.commit()
    

    # Inserting New Records in a Particular Table         
    def insert_new_record(self,record):
        table=input("Enter the table(Books,Students) name where the record is to be inserted\n")
        if table == "Books":
            self.cursor.execute('INSERT INTO Books Values (?, ?, ?, ?, ?) ',[record.book_id,record.name,record.author,record.department,record.student_id])
        elif table == "Students":
            self.cursor.execute('INSERT INTO Students Values (?, ?, ?, ?, ?) ',[record.student_id,record.name,record.gender,record.department,record.Book_id])
        else:
            print("No such table found Try Later")
        #Saving Changes Made to Database    
        self.connection.commit()

    
    #Updating Student name in existing database for a given id
    def update_studentname(self):
        name=input("Enter the name to be given")
        id=input("Enter Student_id for the name to be changed")      
        self.cursor.execute('UPDATE Students SET Name = ? WHERE student_id=?',[name,id])
        self.cursor.execute('SELECT name FROM Students WHERE student_id = ?',[id,])
        output=self.cursor.fetchall()
        if (len(output)) == 0:
            print("No such id in database")
        else:
            for data in output:
                print(data)
        self.connection.commit()

    #Delete Rocords from input Table_name    
    def delete_records(self,table_name):
        if table_name == "STUDENTS":
            pkey ="student_id"
            fkey ="book_id"
            value=input("Enter the Value of student_id associated")
        if table_name == "BOOKS":
            pkey ="book_id"
            fkey ="student_id"
            value=input("Enter the Value of book_id associated")
        try:
            #Check whether the given key values exist in DataBase
            self.cursor.execute("SELECT %s FROM %s WHERE %s = '%s'"% (fkey,table_name,pkey,value))
            output=self.cursor.fetchall()
        except:
            print("Invalid table or value entered")
            return
        if output == []:
            print("No such id or Table Found Check again")
            return
        # CHECK TO ENSURE THE NULL VALUE IS PRESENT TO DELETE RECORD
        elif (None,) not in output:
            if table_name == "BOOKS":
                print("Book cannot be removed because it has been issued by some student")
            if table_name == "STUDENTS":
                print("Student cannot be removed as he has issued some book")
                return
        else:
                #DELETE RECORDS FOR THE GIVEN VALUE
            self.cursor.execute('DELETE FROM %s WHERE %s = "%s" ' % (table_name,pkey,value))
            self.connection.commit()
        #else:
            #print("No table found")
#NULL =''
#Creating Class object
db = Librarydatabase('Lib3.db')
#STUDENT OBJ for Refrence
#Student1=Student('28','Sachin','M','CV','None')
#Student2=Student('36','Vicky','M','ECE','None')
#db.insert_new_record(Student1)
#db.insert_new_record(Student2)

#Basic Console to Start the Program
def start_program():
    choice=int(input("1:To query Database \n2. To delete Records Specifically without query \n3.Update student name for a id\n4.Terminate Program\n"))
    while choice != 4:
        if choice == 1:
            db.query()
            start_program()
        if choice == 2:
            tb_name=input("Enter the table name IN CAPITALS to delete records from")
            db.delete_records(tb_name)
            start_program()
        if choice == 3:
            db.update_studentname()
            start_program()
        
    exit()
start_program()
