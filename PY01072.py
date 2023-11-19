from itertools import combinations

def list_combinations():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = list(set(A))  
    A.sort()
    for comb in combinations(A, K):
        print(' '.join(map(str, comb)))

list_combinations()
