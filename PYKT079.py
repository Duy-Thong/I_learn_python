n=int(input())
for _ in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    a.sort()
    cnt=0
    for i in range(min(a),max(a)+1):
        if i not in a:
            cnt+=1
    print(cnt)   