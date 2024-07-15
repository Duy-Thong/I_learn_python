def calc_continuous_length(N, A):
    res = [1] * N
    stack = [0]
    for i in range(1, N):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        if stack:
            res[i] = i - stack[-1]
        else:
            res[i] = i + 1
        stack.append(i)
    return res

t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    result = calc_continuous_length(N, A)
    print(*result)
