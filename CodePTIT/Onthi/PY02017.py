def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_odd_occurrence(arr)
    print(result)
