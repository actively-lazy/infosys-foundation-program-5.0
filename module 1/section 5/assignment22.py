courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
electives = ("Business Intelligence", "Big Data Analytics")
print("number of courses opted by John = ",len(courses))
print("all courses opted by john = ",courses)
new_courses = []
for cour in courses:
    new_courses.append(cour)
for elec in electives:
    new_courses.append(elec)
print("new courses = ", new_courses)
