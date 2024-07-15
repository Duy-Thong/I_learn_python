def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_superior_prime(n):
    digits = list(map(int, str(n)))
    number_of_digits = len(digits)

    if not is_prime(number_of_digits):
        return "NO"
    
    prime_digits = sum(is_prime(digit) for digit in digits)
    non_prime_digits = number_of_digits - prime_digits

    if prime_digits > non_prime_digits:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_superior_prime(n))
