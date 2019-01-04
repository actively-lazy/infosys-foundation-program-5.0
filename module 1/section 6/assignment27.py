def sum_natural( number):
    sum = 0
    for i in range(1,number+1):
        sum += i
    print("sum = ",sum)
def fibo_series(n):
    fibo0 = 0
    fibo1 = 1
    sum = 0
    for i in range(0,n):
        print(fibo0)
        sum = fibo1+fibo0
        fibo0 = fibo1
        fibo1 = sum
sum_natural(int(input("Enter n: ")))
fibo_series(int(input("Enter n: ")))