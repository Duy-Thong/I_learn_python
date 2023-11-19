def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_occurrences():
    N = int(input())
    A = list(map(int, input().split()))
    primes = {}
    for num in A:
        if is_prime(num):
            if num not in primes:
                primes[num] = 1
            else:
                primes[num] += 1
    for prime, count in primes.items():
        print(f"{prime} {count}")

count_prime_occurrences()
