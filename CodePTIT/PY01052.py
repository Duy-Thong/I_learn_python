import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def digit_sum(N):
    return sum(map(int, str(N)))

T = int(input())

for _ in range(T):
    N = int(input())
    sum_of_digits = digit_sum(N)
    result = "YES" if is_prime(sum_of_digits) else "NO"
    print(result)
