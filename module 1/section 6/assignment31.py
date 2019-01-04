f = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile1.txt","r")
f2 = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile2.txt","w")

for line in f:
    line =line.replace('"','\\"')
    f2.write(line)
f.close()
f2.close()
f = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile1.txt","r")
f2 = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile2.txt","r")
print(f.read())
print(f2.read())
f.close()
f2.close()

