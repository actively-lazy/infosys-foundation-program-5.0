def sum_of_number(n):
    try:
        n = int(n)
        1 / (n + abs(n))
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        if n<0:
            print("n is negative number")
        else:
            print("n is zero")
    else:
        sum = 0
        for i in range(1,n+1):
            sum += i
        print(sum)

sum_of_number('a')
sum_of_number(0)
sum_of_number(-1)
sum_of_number(10)