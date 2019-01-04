def print_multiple(n):
    for i in range(1,n+1):
        print(3*i)
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
print_multiple(int(input("Enter n :")))
print(reverse(input("Enter string: ")))
print(is_palindrome(input("Enter string: ")))