try:
    f = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile1.txt","r")
except IOError:
    print("could not read file 1")
try:
    f2 = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile2.txt","w")
except IOError:
    print("could not write to file 2")
# try:
#     f3 = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile2.txt","r")
# except IOError:
#     print("could not write to file 2")
for line in f:
    line =line.replace('"','\\"')
    f2.write(line)
f2.close()
f.close()
try:
    f = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile1.txt","r")
except IOError:
    print("could not read file 1")
try:
    f2 = open("C:\\Users\\Aldridge\\PycharmProjects\\infosystraining\\venv\\Include\\TestFile2.txt","r")
except IOError:
    print("could not read  file 2")
print(f.read())
print(f2.read())
f2.close()
f.close()

