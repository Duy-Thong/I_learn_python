def is_divisible_by_3(N):
   
    digit_sum = sum(int(digit) for digit in str(N))
    if digit_sum % 3 == 0:
        return "YES"
    else:
        return "NO"
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    result = is_divisible_by_3(N)
    results.append(result)
for result in results:
    print(result)