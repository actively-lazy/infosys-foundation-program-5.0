import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute("SELECT * FROM Employer")
print(cur.fetchall())
print("\nNumber of rows fetched =",cur.rowcount)
print("\nDescription:",cur.description)
cur.close()
con.close()
