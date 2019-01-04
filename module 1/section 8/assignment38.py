
def traveler():
     # global traveler_id,traveler_name,baggage_weight,expiry_year,noc_status

     try:
        traveler_id = int(input("Enter traveler id: "))
        1/(traveler_id+abs(traveler_id))
     except ValueError:
         print("Invalid id")
     except ZeroDivisionError:
         if traveler_id<0:
            print("id is negative number")
            traveler_id =0
     traveler_name = (input("Enter traveler name: "))
     try:
        baggage_weight = int(input("Enter baggage weight: "))
        1/(baggage_weight+abs(baggage_weight))
     except ValueError:
         print("not a number")
         baggage_weight=0
     except ZeroDivisionError:
         if baggage_weight < 0:
             print("baggage weight is negative number")
             baggage_weight=0
     try:
        expiry_year = int(input("Exipry Year: "))
        1/(expiry_year+abs(expiry_year))
     except ValueError:
         print("not a number")
         expiry_year=0
     except ZeroDivisionError:
         if expiry_year < 0:
             print("expiry year is negative number")
             expiry_year=0
     noc_status = (input("Noc Status: "))
     print("Traveler id = " , traveler_id)
     print("Traveler name = " , traveler_name)
     if (check_baggage(baggage_weight) and check_immigration(expiry_year) and check_security(noc_status)):
         print("Allow Traveler to fly")
     else:
         print("Detain Traveler for Rechecking")
def check_baggage(baggage_weight):
    if baggage_weight >=0 and baggage_weight <= 40:
        return True
    else:
        return False
def check_immigration(expiry_year):
    if expiry_year >=2001 and expiry_year <= 2025:
        return True
    else:
        return False
def check_security(noc_status):
    if noc_status =='valid' or noc_status == 'VALID':
        return True
    else:
        return False
traveler()