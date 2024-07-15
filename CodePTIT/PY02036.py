from math import gcd
n = int(input())
A= list(map(int,input().split(" ")))
A.sort()
def is_coprime(a, b):
        return gcd(a, b) == 1

pairs = []
for i in range(n):
    for j in range(i+1, n):
        if is_coprime(A[i], A[j]):
            pairs.append((A[i], A[j]))
s=[]
for pair in pairs:
    s.append(str(pair[0]) + " " + str(pair[1]))
for i in s:
    print(i)
