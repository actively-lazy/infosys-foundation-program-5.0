with open("C:\\Users\Aldridge\PycharmProjects\infosystraining\\venv\Include\\rhyme.txt","r") as f:
    with open("C:\\Users\Aldridge\PycharmProjects\infosystraining\\venv\Include\\words.txt", "w") as f2:
        dict = {}
        for line in f:
            line = line.lower()
            l = line.split(" ")
            l[len(l) - 1] = l[len(l) - 1][0:len(l[len(l) - 1]) - 1]
            for element in l:
                if element in dict.keys():
                    dict[element] += 1
                else:
                    dict[element] = 1
        f2.write(str(dict))
print(dict)