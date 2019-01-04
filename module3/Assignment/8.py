import cx_Oracle

con = cx_Oracle.connect('system','******','localhost:1522/XE')
cur = con.cursor()
cur.execute('drop table Account')

cur.execute("""create table Account(
            CustomerId number(10) primary key,
            AccountNo varchar2(15) not null,
            AccountType varchar2(15) check(AccountType in ('Savings','Current','Recurring')),
            Balance number(12)
            )""")

cur.executemany("insert into Account values(:1,:2,:3,:4)",
                [(101,'IBI1001','Savings',0),(102,'IBI1002','Current',1200),
                 (103,'IBI1003','Savings',6543),(104,'IBI1004','Recurring',7500),
                 (105,'IBI1005','Current',0)])

cur.execute('''select customerid, balance from Account where
            balance=(select max(balance) from account)''')
print(cur.description)
print(cur.fetchall())

cur.execute('select balance from Account where CustomerId=102')
acct_bal = int(cur.fetchall()[0][0])
print(acct_bal)

acct_bal+=2000
cur.execute('update Account set balance=:1 where CustomerId=102',[(acct_bal)])

cur.execute('select balance from Account where CustomerId=102')
print(cur.fetchall()[0][0])

cur.execute("delete from Account where balance=0 and AccountType='Current'")

con.commit()
cur.close()
con.close()
