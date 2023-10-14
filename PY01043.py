def find_numbers(N):
    result = []
    for i in range(11, N):
        digits = str(i)
        palindrome = int(digits + digits[::-1])
        if palindrome >= N:
            break
        if palindrome % 2 == 0:
            result.append(palindrome)
    return result

# Đọc số bộ test
T = int(input())
results = []

# Đọc và giải từng bộ test
for _ in range(T):
    N = int(input())
    result = find_numbers(N)
    results.append(result)

# In kết quả
for result in results:
    print(result)