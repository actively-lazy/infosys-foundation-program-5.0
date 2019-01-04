str = input("Enter String: ")
str = str.upper()
sum = 0

for alphabets in range(65,97):
    for ch in str:
        if chr(alphabets)==ch:
            sum += 1
    if  sum>0 :
        print(sum,chr(alphabets))
    sum = 0




