with open("C:\\Users\Aldridge\PycharmProjects\infosystraining\\venv\Include\student_details.txt","r") as f:
    dict = {}
    list_number = []
    list_name = []
    index = 0
    for line in f:
        l = line.split(" ")
        l[len(l) - 1] = l[len(l) - 1][0:len(l[len(l) - 1]) - 1]
        dict[l[0]] = l[1]
        list_number.append(l[0])
        list_name.append(l[1])
        index += 1
print(dict)
print(list_number)
print(list_name)