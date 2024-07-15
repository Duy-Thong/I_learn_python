import math
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_krish_number(N):
    digit_sum = 0
    original_N = N
    while N > 0:
        digit = N % 10
        digit_sum += factorial(digit)
        N //= 10
    return digit_sum == original_N

T = int(input())

for _ in range(T):
    N = int(input())
    result = "Yes" if is_krish_number(N) else "No"
    print(result)
