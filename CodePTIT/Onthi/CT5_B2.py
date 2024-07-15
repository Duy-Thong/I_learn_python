n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
b=(list(set(a)))
b.sort()
idx = b.index(x)+1
print(idx)
