def check(s):
    a=s[0]+s[1]
    l=len(s)
    b=s[l-2]+s[l-1]
    if a==b:
        return "YES"
    else:
        return "NO"
t=int(input())
for i in range(t):
    s=input()
    print(check(s))