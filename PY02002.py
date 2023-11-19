def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def print_fibonacci_range(t, test_cases):
    fib = fibonacci(93)
    for _ in range(t):
        a, b = test_cases[_]
        for i in range(a, b+1):
            print(fib[i], end=' ')
        print()

t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(list(map(int, input().split())))
print_fibonacci_range(t, test_cases)
