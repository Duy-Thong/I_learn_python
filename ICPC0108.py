def count_triplets(array, n):
    array.sort()
    count = 0
    for i in range(0, n-1):
        left = i + 1
        right = n - 1
        x = array[i]
        while left < right:
            if x + array[left] + array[right] == 0:
                count += 1
                left += 1
                right -= 1
            elif x + array[left] + array[right] < 0:
                left += 1
            else:
            
                right -= 1
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    array = list(map(int,input().split()))
    print(count_triplets(array, n))
