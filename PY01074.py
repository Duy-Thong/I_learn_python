def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def prime_factors_using_sieve(n, primes):
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)
    return factors

def sum_of_prime_factors(n, primes):
    factors = prime_factors_using_sieve(n, primes)
    return sum(factors)

N = int(input())
limit = 10**7
primes = sieve_of_eratosthenes(limit)
result = 0
for _ in range(N):
    num = int(input())
    result += sum_of_prime_factors(num, primes)
print(result)
