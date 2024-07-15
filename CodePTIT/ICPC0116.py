t=int(input())
for _ in range(t):
    s=input()
    res = "YES" if s[0]==s[len(s)-1] else "NO"
    print(res)