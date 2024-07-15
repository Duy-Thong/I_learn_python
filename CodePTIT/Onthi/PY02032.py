s=input()
if len(s)%2==1:
    s=s[:-1]
a=[]
for i in range(0,len(s),2):
    tmp=s[i]+s[i+1]
    a.append(int(tmp))
a.sort()
b=set(a)
print(*sorted(b))