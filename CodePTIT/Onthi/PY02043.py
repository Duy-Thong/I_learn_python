def count_occurrences(S, N):
    cnt=S.count(str(N))
    return cnt
t = int(input())
for _ in range(t):
    S = input()
    N = int(input())
    print(count_occurrences(S, N))  
