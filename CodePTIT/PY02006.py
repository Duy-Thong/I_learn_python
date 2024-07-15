T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if all(a <= b for a, b in zip(A, B)):
        print("YES")
    else:
        print("NO")
