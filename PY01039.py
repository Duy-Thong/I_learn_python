def check(s):
    cnt = 0
    a=[]
    for i in s:
        if i not in a:
            cnt+=1
            a.append(i)
        if cnt>2:
            return False
    for i in range(0, len(s)-2):
        if s[i]!=s[i+2]:
            return False
    return True


t=int(input())
while t>0:
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")
    t-=1

