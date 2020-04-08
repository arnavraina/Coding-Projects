import sqlite3
from Student import Student
from Book import Book
#Student1=Student('20','Arnav','M','CS','10')

class Librarydb:
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
    def update_name(self):
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
        self.cursor.execute('SELECT name from sqlite_master where type= "table"')
        output=self.cursor.fetchall()
        print(type(output))
        #if table_name in output:
        value=input("Enter the Value of student_id associated")
        try:
            self.cursor.execute("SELECT book_id FROM %s WHERE student_id = '%s'"% (table_name,value))
            output=self.cursor.fetchall()
        except:
            print("Invalid table or value entered")
            return
        if output == []:
            print("No such Student_id or Table Found Check again")
            return
        else:
                    #self.cursor.execute('DELETE FROM STUDENTS WHERE student_id = 20')
            self.cursor.execute('DELETE FROM %s WHERE student_id = "%s" ' % (table_name,value))
            self.connection.commit()
        #else:
            #print("No table found")
#NULL =''
#Book obj for Refrence
#Book1=Book('59','Computer Organization','Rajesh Kumar','CS',NULL)
#Creating Class object

db = Librarydb('Lib3.db')
#db.query()
#STUDENT OBJ for Refrence
#Student1=Student('20','Arnav','M','CS','10')
#db.insert_new_record(Book1)

#Basic Console to Start the Program
def start_program():
    choice=int(input("1:To query Database \n 2. To delete Records Specifically without query \n 3.Update student name for a id\n 4.Terminate Program\n"))
    while choice != 4:
        if choice == 1:
            db.query()
            start_program()
        if choice == 2:
            tb_name=input("Enter the table name to delete records from")
            db.delete_records(tb_name)
            start_program()
        if choice == 3:
            db.update_name()
            start_program()
        
    exit()
start_program()
