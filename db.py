import sqlite3

db = sqlite3.connect("mydb.db")#it works on 2 ways agr db nhi h new create krega agr h to connectivity krega

cursor = db.cursor()# it need to perform all sql query it create  object to perfom query in db
#create table
sql = "CREATE TABLE  IF NOT EXISTS  student(id integer  primary key autoincrement ,  name text,age text ,gender text)"#  if not exist work when table is already created then it doestnot occur an error if table already exist it shoew that otherise create new table
cursor.execute(sql) #it execute the query using execute
#insert data into table

insert = "insert into student(name,gender,age) values('shweta','f','19')"


cursor.execute(insert) #it execute the query using execute    

#select the data 
 select = select * from      
           
db.commit()#it save data in data base then display it
