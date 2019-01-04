fibo = []
fibo1 = 0
fibo2 = 1
n = int(input("Input n: "))
if n==1:
    print(fibo)
else:
    for i in range(0,n):
        fibo.append(fibo1)
        sum = fibo2 + fibo1
        fibo1 = fibo2
        fibo2 = sum
print(fibo)