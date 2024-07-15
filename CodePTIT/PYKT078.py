t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    idx = a.index(max(a))
    a.insert(idx,m)
    neg = [ x for x in a if x < 0 ]
    pos = [ x for x in a if x >= 0 ]
    print(*neg,*pos)