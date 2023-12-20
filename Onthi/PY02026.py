n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort
b.sort
a=set(a)
b=set(b)
if a.intersection(b) ==a:
    print("YES")
else:
    print("NO")