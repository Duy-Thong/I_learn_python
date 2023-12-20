def max_accuracy(t, tests):
    results = []
    
    for _ in range(t):
        n = tests[_][0]
        u = tests[_][1]
        p = sorted(tests[_][2], reverse=True)
        
        max_accuracy = 0.0
        remaining_time = u
        
        for i in range(n):
            if remaining_time >= (n - i) * p[i]:
                remaining_time -= (n - i) * p[i]
                max_accuracy += p[i]
            else:
                max_accuracy += remaining_time / (n - i)
                break
        
        results.append(max_accuracy)
    
    return results

# Input
t = int(input())
tests = []

for _ in range(t):
    n = int(input())
    u = float(input())
    p = list(map(float, input().split()))
    tests.append((n, u, p))

# Output
results = max_accuracy(t, tests)

for result in results:
    print("{:.6f}".format(result))
