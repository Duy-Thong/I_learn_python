def is_palindrome(n):
    return str(n) == str(n)[::-1]

def all_digits_even(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

def even_number_of_digits(n):
    return len(str(n)) % 2 == 0

def generate_numbers(N):
    for i in range(22, N):
        if is_palindrome(i) and all_digits_even(i) and even_number_of_digits(i):
            print(i, end=" ")

test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    generate_numbers(N)
    print()
