import math

def years_to_reach_amount(N, X, M):
    years = 0
    while N < M:
        interest = N * (X / 100)
        N += interest
        years += 1
    return years

num_tests = int(input())

for _ in range(num_tests):
    N, X, M = map(float, input().split())
    result = years_to_reach_amount(N, X, M)
    print(result)
