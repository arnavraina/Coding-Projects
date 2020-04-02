import pandas as pd
import sqlite3
Students = {'Name': ['Rajesh','Rohit','Neha','Preeti'],'CGPA': [8.2,7.9,7.1,7.7]}

df = pd.DataFrame(Students, columns= ['Name', 'CGPA'])
df.to_csv('my.csv',encoding='utf-8')
#print (df)
df = pd.read_csv('my.csv')
conn = sqlite3.connect('studentdb1.db')
c=conn.cursor()
#//check if table is already defined. If noty, create it.;
#c.execute('CREATE TABLE Students(Name,CGPA)')
conn.commit()
df.to_sql('Students',conn,if_exists='replace', index = False)
c.execute('SELECT * FROM Students')
a=c.fetchall()
print(a)
for row in c.fetchall():
    print(row)