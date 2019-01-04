import cx_Oracle

def maxl(uid):
    return "select picid from pdetails where likes = (select max(likes) from pdetails where userid="+uid+")"

def minl(uid):
    return "select picid from pdetails where likes = (select min(likes) from pdetails where userid="+uid+")"

def lmost(uid, cur):
    s1 = "select picid from pdetails where userid="+uid
    cur.execute(s1)
    t1 = cur.fetchall()
    t2 = list()
    for i in t1:
        t2.append(i[0])
    s2 = "select userid,count(userid) from liked group by userid, picid having picid in ("+','.join(map(str, t2))+")"
    cur.execute(s2)
    l1,l2=-1,-1
    t3 = cur.fetchall()
    for i in t3:
        if(i[1]>l2):
            l2=i[1]
            l1=i[0]
    return l1

def mpics(uid):
    return "select picid from ptags where tag='Music'"

def poptag():
    return "select tag from ptags group by tag having count(tag)=(select max(count(tag)) from ptags group by tag)"

def uliked():
    return "select userid from pdetails group by userid having sum(likes)=(select max(sum(likes)) from pdetails group by userid)"

def tagold(uid):
    return "insert into ptags select picid, 'Old' from pdetails where extract(year from sysdate)-extract(year from postdate)<3 and userid="+uid

def delinactive(cur):
    s1 = "select userid from pdetails group by userid,postdate having sysdate-postdate>365"
    cur.execute(s1)
    t1 = cur.fetchall()
    t2 = list()
    for i in t1:
        t2.append(i[0])

    ustr = ','.join(map(str, t2))

    if not ustr=="":
        s2 = "delete from useremail where userid in ("+ustr+")"
        #assuming all references to 'userid' have 'ON DELETE CASCADE' option
        cur.execute(s2)
    return "Complete"
    
try:
    con = cx_Oracle.connect('system','******','localhost:1522/XE')
except cx_Oracle.DatabaseError as er:
    print("Invalid credentials -",er)
cur = con.cursor()

uid = input("Enter user id- ")
print("""Queries
        1. Max Liked pic
        2. Min Liked pic
        3. Who liked most of my pics
        4. 'Music' tagged pics
        5. Most popular tag
        6. Most liked user
        7. Tag old pictures
        8. Delete inactive users""")
qn = int(input("Enter query number- "))

dictn = {
    1:maxl(uid),
    2:minl(uid),
    3:lmost(uid, cur),
    4:mpics(uid),
    5:poptag(),
    6:uliked(),
    7:tagold(uid),
    8:delinactive(cur)
    }
strn = dictn[qn]
print("\nResult(s)")
try:
    if not (qn==3 or qn==8):
        cur.execute(strn)
    else:
        print(str)
    if cur:
        for row in cur:
            print(*row)
except cx_Oracle.InterfaceError as er2:
    pass
except cx_Oracle.DatabaseError as er:
    print("Invalid command -",er)

cur.close()
con.commit()
con.close()
