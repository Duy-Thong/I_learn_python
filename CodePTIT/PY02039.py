N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
K = int(input())

upper_half_sum = 0
lower_half_sum = 0

for i in range(N):
    for j in range(N):
        if i <  N-j-1:
            upper_half_sum += matrix[i][j]
        elif i > N- j-1:
            lower_half_sum += matrix[i][j]

difference = abs(upper_half_sum - lower_half_sum)

if difference <= K:
    print("YES")
else:
    print("NO")

print(difference)
