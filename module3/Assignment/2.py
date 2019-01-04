import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()

cur.execute("select companyname, emailid from employer where city='Bangalore'")
print(cur.fetchall())

city = input("Enter city ")

cur.execute("select companyname, mobile, emailid from employer where renewalstatus=:1 and city=:2",("Active",city))
print(cur.fetchall())

cur.execute("select companyname, mobile, emailid from employer where renewalstatus=:1 and city=:2",(city,"Active"))
print(cur.fetchall())

cur.execute("select companyname, mobile, emailid from employer where renewalstatus=:p1 and city=:p2",{'p1':"Active",'p2':city})
print(cur.fetchall())

cur.execute("select companyname, mobile, emailid from employer where renewalstatus=:p1 and city=:p2",{'p2':city,'p1':"Active"})
print(cur.fetchall())

cur.close()
con.close()
