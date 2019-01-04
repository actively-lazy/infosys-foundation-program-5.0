mylist = [1,2,3,"4",5]
sum = 0
for i in mylist:
    try:
        sum = sum + i
    except TypeError:
        sum = sum + int(i)
print(sum)
try:
    print(mylist[5])
except IndexError:
    print("index out of range")

