for i in range(50,81):
    if i%2 == 0:
        print(i)
print("--------------------------------------------------------------------------------------------")
n = int(input("Input n: "))
sum = 0
for i in range(1,n+1):
    sum += i
print("sum = ",sum)
print("--------------------------------------------------------------------------------------------")
n = int(input("Input n: "))
for i in range(2,n):
    if n%i == 0:
        print("Number is not prime")
        break;
else:
    print("number is prime")
print("--------------------------------------------------------------------------------------------")
fibo1 = 0
fibo2 = 1
n = int(input("Input n: "))
if n==1:
    print(1)
else:
    for i in range(0,n):
        print(fibo2)
        sum = fibo2 + fibo1
        fibo1 = fibo2
        fibo2 = sum

