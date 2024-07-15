from itertools import combinations
def team_name_combinations():
    N, K = map(int, input().split())
    names = input().split()
    unique_names = sorted(set(names)) 
    comb = combinations(unique_names, K) 
    for c in comb:
        print(" ".join(c))

team_name_combinations()
