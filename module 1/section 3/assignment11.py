from math import pi
print("--------------------------------------------------------------------------------------------")
a = 4
b = 5
print("values before swapping: a = %d , b = %d" %(a,b) )
a=a+b
b=a-b
a=a-b
print("values after swapping: a = %d , b = %d" %(a,b) )
print("--------------------------------------------------------------------------------------------")
print("Enter marks obtained in 3 subjects")
sub1 = int(input("Subject 1 marks: "))
sub2 = int(input("Subject 2 marks: "))
sub3 = int(input("Subject 3 marks: "))
avg = ( sub1 + sub2 + sub3 ) / 3
print("average = ",avg)
print("--------------------------------------------------------------------------------------------")
print("Enter radius of circle ")
radius = float(input("radius: "))
area = pi*radius*radius;
perimeter = 2*pi*radius
print("area = ",area)
print("perimeter = ",perimeter)
print("--------------------------------------------------------------------------------------------")
num_of_hr = 40
pay_rate = 400
num_of_week = 4
monthly_pay =   num_of_hr * pay_rate * num_of_week
print("number of hr = ",num_of_hr)
print("pay rate = ",pay_rate)
print("number of week per month = ",num_of_week)
