import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute('drop table Vehicle2')
cur.execute("""create table Vehicle2(
            Vehicleid number(5) primary key,
            Vehiclename varchar2(10)
            )""")
base = 2001
cur.executemany("insert into Vehicle2 values(:1,:2)",
                [(base,'Toyota'),(base+1,'Maruti'),
                 (base+2,'Nissan'),(base+3,'Hyundai')])

cur.executemany("insert into Vehicle2 values(:p1,:p2)",
                [{'p1':base+4,'p2':'Honda'},
                 {'p1':base+5,'p2':'Volkswagen'}])

cur.execute('select * from Vehicle2')
print(cur.fetchall())
cur.close()
con.commit();
con.close()
