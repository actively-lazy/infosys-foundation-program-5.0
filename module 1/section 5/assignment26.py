java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}
print("python course",python_course)
print("java only",java_course-python_course)
print("python only",python_course-java_course)
print("both java and python" , java_course & python_course)
print("either java and python but not both" , (java_course | python_course)-(java_course & python_course))
print("either java and python" , (java_course | python_course))


