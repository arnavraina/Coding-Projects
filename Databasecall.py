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
    def delete_records(self,table_name):
        '''
        value = 20
        column_name = "student_id"
        '''
        self.cursor.execute('SELECT name from sqlite_master where type= "table"')
        output=self.cursor.fetchall()
        for idx in range(len(output)):
            #print(output[idx])
            if table_name in output[idx]:
                value=input("Enter the Value to be Deleted")
                column_name=input("Enter the column name for the susquent value")
                #self.cursor.execute('DELETE FROM STUDENTS WHERE student_id = 20')
                self.cursor.execute('DELETE FROM %s WHERE %s = %s ' % (table_name, column_name, value))
                self.connection.commit()
                #self.cursor.execute('DELETE FROM STUDENTS WHERE student_id = ? ',[value])
                '''
                elf.cursor.execute("SELECT * FROM STUDENTS")
                self.connectiosn.commit()
                # COmment outS
                #self.cursor.execute("SELECT * FROM STUDENTS")
                outputx=self.cursor.fetchall()
        #rint(len(output))
                for data in outputx:
                    print(data)
                self.connection.commit()
                '''

Book1=Book('33','MicroProcessors','T G Basvaraju','ECE','29')
#db = Librarydb(database='Lib3.db')

db = Librarydb('Lib3.db')
#db.query()
#db.query()
Student1=Student('20','Arnav','M','CS','10')
#db.insert_new_record(Book1)
db.query()
db.delete_records('BOOKS')
db.query()
#db.delete_records('STUDENTS')SELECT SELECT COLUMN_NAME.
#PRAGMA table_info(STUDENTS)

