import sqlite3

conn = sqlite3.connect('Lib2.db')
c=conn.cursor()

i=input("Press 1 for displaying all records \n Press 2 For Finding student and book id for the given Book issued\n")
if i == "1":
    c.execute('SELECT * FROM Books')
    data = c.fetchall()
    print("Books Record")
    for row in data:
        print(row)
    c.execute('SELECT * FROM STUDENTS')
    print("Students Record")
    data = c.fetchall()
    for row in data:
        print(row)
if i == "2":
    print("Enter the Book_name")
    bk_name=input()
    print(len(bk_name))
    c.execute('SELECT Book_id,Student_id FROM Books WHERE Book_name = ?',(bk_name,))
    data=c.fetchall()
    for row in data:
        print(row)
conn.close()

# connect to database
def connectToDb:
    conn = sqlite3.connect('Lib2.db')
    return conn.cursor()

main 
    conn_link = connectToDb()
    
# connect to db
