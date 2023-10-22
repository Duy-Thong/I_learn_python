T = int(input())

for _ in range(T):
    N = input()
    digits = list(map(int, N))

    even_sum = 0
    odd_product = 1
    all_odd_zeros = True

    for i in range(len(digits)):
        if i % 2 == 0:
            even_sum += digits[i]
        else:
            if digits[i] != 0:
                odd_product *= digits[i]
                all_odd_zeros = False

    if all_odd_zeros:
        odd_product = 0

    print(even_sum, odd_product)