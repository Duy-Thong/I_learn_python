from math import gcd
t = int(input())
a=[int(i) for i in input().split()]
a.sort()
s=""
for i in range(len(a)):
   for j in range(i+1,len(a)):
        if gcd(a[i],a[j])==1:
            s+=str(a[i])+" "+str(a[j])+"\n"
print(s)