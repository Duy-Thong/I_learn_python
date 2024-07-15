n=int(input())
k=n %4096
m=n//4096
if k !=0:
    print((m+1)*4)
else:
    print(m*4)