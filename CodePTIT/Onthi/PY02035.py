s=input()
k=int(input())
if len(s)%2==1:
    s=s[:-1]
a=[]
for i in range(0,len(s),2):
    tmp=s[i]+s[i+1]
    a.append(int(tmp))
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
b=sorted(b.items(),key=lambda x:x[0])
check=False
for i in b:
    if i[1]>=k:
        print(i[0],i[1])
        check=True
if check==False:
    print("NOT FOUND")