with open("C:\\Users\Aldridge\PycharmProjects\infosystraining\\venv\Include\courses.txt","r") as f:
    dict = {}
    list = []
    index = 0
    for line in f:
        l = line.split(" ")
        l[len(l)-1] = l[len(l)-1][0:len(l[len(l)-1])-1]
        for element in l:
            dict[index] = element
            list.append(element)
            index +=1

print(dict)
print(list)