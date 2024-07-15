def find_smallest_missing(N, A):
    A.sort()
    missing = 1
    for i in range(N):
        if A[i] == missing:
            missing += 1
        else:
            break
    return missing

N = int(input())
A = list(map(int, input().split()))
print(find_smallest_missing(N, A))
