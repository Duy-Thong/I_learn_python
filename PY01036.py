def calculate_sum(N):
    if N % 2 == 0:  
        S = sum(1 / i for i in range(2, N + 1, 2))
    else:  
        S = sum(1 / i for i in range(1, N + 1, 2))
    return S


num_tests = int(input())
results = []

for _ in range(num_tests):
    N = int(input())
    result = calculate_sum(N)
    results.append(result)
for result in results:
    print(f'{result:.6f}')
