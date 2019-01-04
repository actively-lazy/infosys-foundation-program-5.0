import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute('''update Vehicle2 set Vehicleid=Vehicleid-1000 where
            Vehicleid between 2001 and 2006''')

cur.execute('''update Vehicle2 set Vehiclename='Mahindra' where
            Vehicleid=1003''')

cur.execute('select * from Vehicle2')
print(cur.fetchall())
cur.close()
#con.commit();
con.close()
