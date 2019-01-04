import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute('drop table Users')
cur.execute("""create table Users(
            UserId number(10) primary key,
            Username varchar2(30) not null,
            Password varchar2(20) not null,
            UserType varchar2(20) check(UserType in ('Employer','Jobseeker'))
            )""")

cur.execute("""insert into Users values(1,'jobs@infosys.com', 'jobs@infosys',
                'Employer')""")

uid = 2
name = 'careers@accenture.com'
passw = 'Acc1'
utype = 'Employer'
cur.execute('insert into Users values(:1,:2,:3,:4)',(uid,name,passw,utype))

uid = 3
name = 'rahulitsme@gmaill.com'
passw = 'rahulindia93'
utype = 'Jobseeker'
cur.execute("""insert into Users
        values(:p1,:p2,:p3,:p4)""",{'p1':uid,'p2':name,'p3':passw,'p4':utype})

uid = int(input("Enter 4th user ID "))
name = input("Enter 4th user name ")
passw = input("Enter 4th user password")
utype = input("Enter 4th user type ")
cur.execute('insert into Users values(:1,:2,:3,:4)',(uid,name,passw,utype))

con.commit()
cur.execute('select * from Users')
for row in cur.description:
    print(row[0], end='\t')
print('')
for row in cur:
    for i in row:
        print(i, end='\t')
    print('')
cur.close()
con.close()
