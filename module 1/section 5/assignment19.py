accepted_string = input("Enter Accepted String: ")
resultant_string = ""
counter = 0
for ch in accepted_string:
    if ch!= " " and counter %2 == 0:
        resultant_string +=  ch
    if ch!=" ":
        counter += 1

expected_output = resultant_string[::-1]
print("accepted string = "+accepted_string)
print("resultant string = "+resultant_string)
print("expected  string = "+expected_output)
