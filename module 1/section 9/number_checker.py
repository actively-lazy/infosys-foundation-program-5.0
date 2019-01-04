def is_prime(num):
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            return False
    return True
def is_even(num):
    if num % 2 == 0:
        return True
    else: return False