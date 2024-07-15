s=input()
if len(s)%2==1:
    s=s[:-1]
a=[]
for i in range(0,len(s),2):
    tmp=s[i]+s[i+1]
    a.append(int(tmp))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(*b)