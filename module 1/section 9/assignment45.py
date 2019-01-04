import re

cust_details = "Hello John, your customer id is j181"

print("a)")
m = re.search(r"^Hello\sJohn", cust_details)
if m:
    print(m.group())
m = re.search(r"^hello\sJohn", cust_details)
if m:
    print(m.group())

print("b)")
m = re.search(r"\S\d\d\d$", cust_details)
print(m.group())

print("c)")
a = re.search(r"j\d\d\d",cust_details)
str = a.group()[1:]
m = re.sub(r"j\d\d\d",str, cust_details)
print(m)

print("d)")
m = re.sub(r"id", r"ID", cust_details)
print(m)
