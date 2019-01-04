
grades = {"John" : 86.5 , "Jack" : 91.2, "Jill": 84.5, "Harry" : 72.1, "Joe" : 80.5 }
print("NAME     GRADE")
for name in grades:
    print(name,"    ",grades[name])
print("Top two scores")
max = 0
for name in grades:
    if grades[name]>max:
        max = grades[name]
        maxname = name
print(maxname,"   ",max)
max = 0
for name in grades:
    if grades[name]>max and name != maxname:
        max = grades[name]
        maxname2 = name
print(maxname2,"   ",max)
sum = 0
for grade in grades.values():
    sum += grade
average = sum / len(grades)
print("Average = ", average)