def solve(n, k):
    count = 0
    for i in range(n + 1):
        s = bin(i)[2:]
        if s.count('0') == k:
            count += 1
    return count
T = int(input())
for _ in range(T):
    n,k = map(int, input().split())
    print(solve(n,k))
