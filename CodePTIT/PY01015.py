def check(s):
    l=len(s)
    for i in range(1,l):
        if s[i]<s[i-1]:
            return False
    return True
t=int(input())
for _ in range(t):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")
    
        