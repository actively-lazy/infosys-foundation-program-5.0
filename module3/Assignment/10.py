import cx_Oracle

try:
    con = cx_Oracle.connect('system','******','localhost:1522/XE')
except cx_Oracle.DatabaseError as er:
    print("Invalid credentials -",er)
cur = con.cursor()

try:
    cur.execute("insert into product values('P106','Jams',150)")
except cx_Oracle.DatabaseError as er:
    print("Invalid command -",er)
cur.close()
con.close()
