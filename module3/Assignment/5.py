import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()

cur.execute('select username, usertype from Users where userid=4')
print(cur.fetchall())
cur.execute("""update Users set username='lookingforjob@yahoo.com',
            usertype='Jobseeker' where userid=4""")
cur.execute('select username, usertype from Users where userid=4')
for row in cur.description:
    print(row[0], end='\t')
print('')
for row in cur:
    for i in row:
        print(i, end='\t')
    print('')

passw = input("Enter user id=1 password ")
cur.execute('select password from Users where userid=1')
for row in cur.description:
    print(row[0], end='\t')
print('')
for row in cur:
    for i in row:
        print(i, end='\t')
    print('')
cur.execute("update Users set password='"+passw+"' where userid=1")
cur.execute('select password from Users where userid=1')
for row in cur.description:
    print(row[0], end='\t')
print('')
for row in cur:
    for i in row:
        print(i, end='\t')
    print('')

con.commit()
cur.close()
con.close()
