def find_character(N, K):
    if N == 1:
        return 'A'
    else:
        length = 2 ** N - 1
        mid = length // 2 + 1
        if K == mid:
            return chr(64 + N)
        elif K < mid:
            return find_character(N - 1, K)
        else:
            return find_character(N - 1, K - mid)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(find_character(N, K))
