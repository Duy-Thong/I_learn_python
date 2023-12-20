def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_index(N, A):
    B = []
    for num in A:
        if num not in B:
            B.append(num)
    for i in range(len(B)):
        if is_prime(sum(B[:i+1])) and is_prime(sum(B[i+1:])):
            return i
    return "NOT FOUND"

N = int(input())
A = list(map(int, input().split()))

result = find_index(N, A)
print(result)
