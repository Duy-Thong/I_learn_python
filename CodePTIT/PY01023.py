def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def format_output(factors):
    factor_counts = {}
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
    
    formatted_result = "1"
    for factor, count in factor_counts.items():
        formatted_result += f" * {factor}^{count}"
    
    return formatted_result
num_tests = int(input())

for _ in range(num_tests):
    n = int(input())
    factors = prime_factorization(n)
    formatted_result = format_output(factors)
    print(formatted_result)
