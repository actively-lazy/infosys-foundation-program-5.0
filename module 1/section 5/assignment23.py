customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
for id in customer_details:
    print("Customer id = ",id," Customer name = ",customer_details[id])
print("Number of customer = ", len(customer_details))
for name in sorted(customer_details.values()):
    print(name)
del customer_details[1005]
print(customer_details)
customer_details[1003] = "Mary"
print(customer_details)
if 1002 in customer_details.keys():
    print("1002 exists in customer details")
else:
    print("1002 does not exists in customer details")
