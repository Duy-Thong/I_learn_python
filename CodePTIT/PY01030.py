
import math
def is_coprime(a, b):
    return math.gcd(a, b) == 1
def generate_numbers(N, K):
    numbers = []
    start = 10 ** (K-1)  
    end = 10 ** K - 1  

    for num in range(start, end+1):
        if is_coprime(num, N):
            numbers.append(num)

    return numbers


N, K = map(int, input().split())
numbers = generate_numbers(N, K)

for i in range(0, len(numbers), 10):
    print(' '.join(str(num) for num in numbers[i:i+10]))
