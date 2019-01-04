furniture_name =["Sofa set", "Dining table", "table stand", "Cupboard"]
furniture_cost =(20000,8500,4599,13920)
bill_amt = 0
for name in furniture_name:
    print(name)
    print("Enter quantity to be bought")
    quantity = int(input("Quantity: "))
    if quantity >=0:
        bill_amt += quantity*furniture_cost[(furniture_name.index(name))]
    else:
        print("Invalid quantity")
        bill_amt = 0
        break
print("bill amt = ",bill_amt)
print("------------------------------------------------------------------------------")
furniture ={"Sofa set":20000, "Dining table":8500, "table stand":4599, "Cupboard":13920}
bill_amt = 0
for name in furniture:
    print(name)
    print("Enter quantity to be bought")
    quantity = int(input("Quantity: "))
    if quantity >=0:
        bill_amt += quantity*furniture[name]
    else:
        print("Invalid quantity")
        bill_amt = 0
        break
print("bill amt = ",bill_amt)





