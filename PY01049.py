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
def is_prime_preferred_number(N):
    num_str = str(N)
    num_len = len(num_str)
    
    prime_count = 0
    non_prime_count = 0
    
    for digit in num_str:
        digit_int = int(digit)
        if is_prime(digit_int):
            prime_count += 1
        else:
            non_prime_count += 1
    if is_prime(num_len):
        if prime_count > non_prime_count:
            return "YES"
    
    return "NO"
t = int(input())
for _ in range(t):
    N = int(input())
    result = is_prime_preferred_number(N)
    print(result)
