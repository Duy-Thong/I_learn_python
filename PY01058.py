def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    N = input()
    last_four_digits = N[-4:]
    last_four_num = int(last_four_digits)

    if is_prime(last_four_num):
        print("YES")
    else:
        print("NO")