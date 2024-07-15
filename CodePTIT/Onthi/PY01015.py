def check(n):
    if len(n)%2==0:
        return 'NO'
    elif n[0]==n[1]:
        return 'NO'
    else :
        x=[ n[i] for i in range(0,len(n),2)]
        if len(set(x))!=1:
            return 'NO'
        else :
            return 'YES'
        
t=int(input())
for _ in range(t):
    n=input()
    print(check(n))
    
