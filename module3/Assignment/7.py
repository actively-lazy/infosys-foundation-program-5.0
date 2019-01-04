import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute("delete from users where userid=1")
inp = input("Enter VehicleID ")
cur.execute("delete from Vehicle where vehicleid=:p1",{'p1':inp})
cur.close()
con.close()
