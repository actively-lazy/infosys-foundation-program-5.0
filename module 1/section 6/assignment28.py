# traveler_id = 0
# traveler_name = ""
# baggage_weight = 0
# expiry_year = 0
# noc_status = False

def traveler():
     # global traveler_id,traveler_name,baggage_weight,expiry_year,noc_status
     traveler_id = int(input("Enter traveler id: "))
     traveler_name = (input("Enter traveler name: "))
     baggage_weight = int(input("Enter baggage weight: "))
     expiry_year = int(input("Exipry Year: "))
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