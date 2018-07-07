import sqlite3

dbs = sqlite3.connect("mydbs.db")#it works on 2 ways agr db nhi h new create krega agr h to connectivity krega
dbs.row_factory = sqlite3.Row# it accsess the data dictionary faomart
cursor = dbs.cursor()# it need to perform all sql query it create  object to perfom query in db
'''#create table
sql = "CREATE TABLE  IF NOT EXISTS  s12(id integer  primary key autoincrement ,  name text,age text ,gender text)"#  if not exist work when table is already created then it doestnot occur an error if table already exist it shoew that otherise create new table
cursor.execute(sql) #it execute the query using execute
#insert data into table

insert = "insert into s12(name,age,gender) values('pooja','20','f')''


cursor.execute(insert)''' #it execute the query using execute         
           
#select the date 
#select = "select  * from  std where id ={}".format(2)
#student = cursor .execute(select)
#print (data)
#print(student.fetchone())
#print(student.fetchall))
#------or-----
#for i in student:
    #print(dict(i))


#for i in student:
    #print(i)
# delete the row data
#delete = "delete from std"
#student = cursor .execute(delete)

#update 
#update ="update s12  set name = '{}' where id ={}".format("shreya",1)#format used to format the string 
#cursor.execute(update)

# 2nd way to insert multiple data insert query in loop
datas =[('shweta','1','f'),('pooja','1','f'),('shreya','1','f'),('priyanka','1','f'),('salu','1','f'),('kalu','1','f'),('shivani','1','f')]

#for i in datas:                                                         
    #ins ="insert into s12(name ,age,gender) values ('{}','{}','{}')".format(i[0],i[1],i[2])
    #cursor.execute(ins)
 #3rd way to insertion insert query run only one time and insert multiple data
d ='';
for i in datas: 
    d=d+",('{}','{}','{}')".format(i[0],i[2],i[1])
#print(d[1:])
print("insert into s12(name,age,gender)values"+d[1:]+"")
cursor.execute("insert into s12(name,age,gender)values"+d[1:]+"")
dbs.commit()#it save data in data base then display it
