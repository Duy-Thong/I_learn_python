from itertools import permutations

def list_permutations(S):
    
    perms = permutations(S)
   
    sorted_perms = sorted(''.join(p) for p in perms)
    for perm in sorted_perms:
        print(perm)

S = input().strip()
list_permutations(S)
