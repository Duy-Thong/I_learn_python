def sort_even_odd(A):
    even = sorted([x for x in A if x % 2 == 0])
    odd = sorted([x for x in A if x % 2 != 0], reverse=True)
    even_index, odd_index = 0, 0

    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i] = even[even_index]
            even_index += 1
        else:
            A[i] = odd[odd_index]
            odd_index += 1
    return A

# Read input
n = int(input())
A = list(map(int, input().split()))

# Sort and output
sorted_A = sort_even_odd(A)
print(*sorted_A)
