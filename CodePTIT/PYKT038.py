def binarytodec(n):
    res=0
    for i in range(len(n)):
        res=res*2+int(n[i])
    return res
n=input()
l=len(n)

k=l%3
if k!=0:
    n='0'*(3-k)+n
res=0
for i in range(0,l,3):
    k=n[i:i+3]
    res=res*10+binarytodec(k)
print(res)
    
