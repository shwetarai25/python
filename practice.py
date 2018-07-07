import sqlite3
db = sqlite3.connect("mypractice.db")
cursor = db.cursor()
#sql = "CREATE TABLE  std(id integer  primary key autoincrement ,  name text,age text ,gender text)"
#cursor.execute(sql)

#sql1= "CREATE TABLE  student_details(id integer  primary key autoincrement ,  address text)"
#cursor.execute(sql1)
#2nd way to insertion 
data = [("shweta","2","f"),("bachha","1","f"),("pooja","10","f"),("aal0 u","1","m"),("bhalu","25","m"),("salu","5","f"),("kalu","10","m")]
datas= ''
for i in data:
    datas = datas +",('{}','{}','{}')".format(i[0],i[1],i[2])

#print(datas[1:])
#print ( "insert into std(name,age,gender) values "+datas[1:])

cursor.execute("insert into std(name,age,gender) values "+datas[1:])
db.commit()
'''
insert = "insert into std(name,age,gender) values('pooja','20','f')''
cursor.execute(insert) #it execute the query using execute

insert1 = "insert into student_detail(address) values('bhilai')''
cursor.execute(insert1)'' 
'''
         
           

