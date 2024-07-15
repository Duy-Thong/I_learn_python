def count_pairs(n, arr):
    count = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
result = count_pairs(n, arr)
print(result)
