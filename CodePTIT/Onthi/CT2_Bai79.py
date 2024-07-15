s1=input()
s=input()
n=int(input())
if len(s)/len(s1)!=n:
    print("NO")
    exit()
if s.count(s1)==n:
    print("YES")
else:
    print("NO")