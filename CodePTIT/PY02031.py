def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if is_prime(matrix[i][j]):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for row in matrix:
    print(*row)
