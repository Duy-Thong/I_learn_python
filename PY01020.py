t=int(input())
for _ in range(t):
    n=input()
    l=len(n)
    if n[l-2]+n[l-1]!="86":
        print("NO")
    else:
        print("YES")