def count_occurrences():
    t = int(input())
    for _ in range(t):
        S = input().strip()
        N = input().strip()
        print(S.count(N))

count_occurrences()
