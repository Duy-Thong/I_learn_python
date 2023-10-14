import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_perfect_prime(N):
    if not is_prime(N):
        return "No"
    
    reversed_N = int(str(N)[::-1])
    
    if not is_prime(reversed_N):
        return "No"
    
    digit_sum = sum(map(int, str(N)))
    
    if not is_prime(digit_sum):
        return "No"
    
    for digit in str(N):
        if not is_prime(int(digit)):
            return "No"
    
    return "Yes"
T = int(input())
for _ in range(T):
    N = int(input())
    result = is_perfect_prime(N)
    print(result)
