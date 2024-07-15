def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_even(num):
    return num % 2 == 0

T = int(input())

for _ in range(T):
    N = input()
    digits = list(map(int, N))
    even_digits = digits[::2]
    odd_digits = digits[1::2]

    if all(is_even(digit) for digit in even_digits) and all(not is_even(digit) for digit in odd_digits) and is_prime(sum(digits)):
        print("YES")
    else:
        print("NO")