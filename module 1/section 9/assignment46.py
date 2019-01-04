import re
student_id = input("Enter student id: ")
if student_id.isdigit():
    student_id = int(student_id)
    student_name = input("Enter student name: ")
    if student_name.isalpha():
        fees_amount = input("Enter fees amount")
        a = re.match(r"^[0-9]*.\d\d$",fees_amount)
        if a.group()==fees_amount:
            print("Student id = ", student_id)
            print("Student name = "+ student_name)
            print("Fees amount = "+ fees_amount)
            print("Email id = "+student_name+"@ABC.com")
        else:
            print("Fees amount not valid")

