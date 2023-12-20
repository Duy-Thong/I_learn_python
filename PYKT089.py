def sort_odd_even(n, A):
    odd = sorted([A[i] for i in range(n) if A[i] % 2 != 0], reverse=True)
    even = sorted([A[i] for i in range(n) if A[i] % 2 == 0])
    
    result = []
    i, j = 0, 0
    for a in A:
        if a % 2 == 0:
            result.append(even[i])
            i += 1
        else:
            result.append(odd[j])
            j += 1
    return result

n = int(input())
A = list(map(int, input().split()))
result = sort_odd_even(n, A)
for i in result:
    print(i, end=' ')
