bill_amt = int(input("Bill amt: "))
discount = 1
if   bill_amt>=1000:
     discount = 5
elif bill_amt>=500:
     discount = 2
print("bill amt = ",bill_amt)
print("discount = ",discount)
print("--------------------------------------------------------------------------------------------")
customer_id = int(input("Customer ID: "))
valid_customer = False
if customer_id>=101 and customer_id<=1000:
    valid_customer = True
print("Customer id = ",customer_id)
print("Valid customer = ",valid_customer)