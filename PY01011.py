import math
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
num_tests = int(input())

for _ in range(num_tests):
    a, b = map(int, input().split())
    gcd_ab = math.gcd(a, b)
    sum_digits_gcd = sum_of_digits(gcd_ab)
    
    if is_prime(sum_digits_gcd):
        print("YES")
    else:
        print("NO")
