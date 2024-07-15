def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sort_prime_numbers(arr):
    primes = [x for x in arr if is_prime(x)]
    primes.sort()
    prime_index = 0
    result = []
    for num in arr:
        if is_prime(num):
            result.append(primes[prime_index])
            prime_index += 1
        else:
            result.append(num)
    return result
N = int(input())
A = list(map(int, input().split()))
result = sort_prime_numbers(A)
print(*result)
