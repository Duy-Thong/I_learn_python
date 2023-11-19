import math

def prime_factors(n):
    """Function to generate prime factors of n"""
    factors = []
    while n % 2 == 0:
        factors.append(2),
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            factors.append(i),
            n = n / i
    if n > 2:
        factors.append(n)
    return factors

def sum_prime_factors(n):
    """Function to sum the prime factors of n"""
    return sum(prime_factors(n))

def main():
    """Main function to input N numbers and output the sum of their prime factors"""
    N = int(input())
    sum_of_prime_factors = 0
    for _ in range(N):
        num = int(input())
        sum_of_prime_factors += sum_prime_factors(num)
    print(int(sum_of_prime_factors))

main()
