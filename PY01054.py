T = int(input())
for _ in range(T):
    N = input()
    product = 1
    for digit in N:
        if digit != '0':
            product *= int(digit)
    print(product)