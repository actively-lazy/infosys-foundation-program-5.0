str = input("Enter String: ")
if str.lower()==str[::-1].lower():
    print("String is palindrome")
else:
    print("String is not palindrome")
print("Actual string = " + str)
print("Reversed string = " + str[::-1])

