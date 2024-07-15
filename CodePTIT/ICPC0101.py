def solve(N, A):
    stack = []

    for num in A:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)

    return len(stack)


N = int(input())
A = list(map(int, input().split()))
result = solve(N, A)
print(result)
