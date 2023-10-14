def is_palindrome(num_str):
    return num_str == num_str[::-1]

def is_palindromic_sum(N):
    sum_of_digits = sum(map(int, str(N)))
    if sum_of_digits <= 9:
        return "NO"
    return "YES" if is_palindrome(str(sum_of_digits)) else "NO"

# Đọc số bộ test
T = int(input())

for _ in range(T):
    N = input()
    result = is_palindromic_sum(N)
    print(result)
