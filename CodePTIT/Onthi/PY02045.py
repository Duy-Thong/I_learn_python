n=int(input())
while len(str(n))!=1:
    s=str(n)
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    n=int(s1)+int(s2)
    print(n)
