def generate_fibo(x):

 if(x == 0):
  return 0
 elif(x == 1):
  return 1
 else:
  return generate_fibo(x-1) + generate_fibo(x-2)

x = int(input("Enter the term till which you wnat to generate fibonacci sequence: "))

for i in range(x):
 print(generate_fibo(i))