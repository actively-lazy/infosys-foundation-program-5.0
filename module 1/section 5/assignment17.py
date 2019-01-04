str1 = input("Enter String1: ")
str2 = input("Enter String2: ")
str3 = str1 + str2
str4 = ""
for i in str3:
    if i.isupper():
        str4 += i
print(str4)