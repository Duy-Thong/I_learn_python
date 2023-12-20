import math

def main():
    n,k=map(int,input().split())
    cnt=0
    for i in range(pow(10,k-1),pow(10,k)):
        if math.gcd(i,n)==1:
            cnt+=1
            print(i,end=" ")
            if cnt==10 :
                print()
                cnt=0
if __name__=="__main__":
    main()