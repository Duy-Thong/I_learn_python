def product_of_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def sort_array_by_digit_product(test_cases):
    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort(key=lambda x: (product_of_digits(x), x))
        print(' '.join(map(str, arr)))

test_cases = int(input())
sort_array_by_digit_product(test_cases)
