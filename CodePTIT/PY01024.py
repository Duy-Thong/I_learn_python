def check(s):
    sum=0
    for i in range(0,len(s)):
        sum+=ord(s[i])-ord('0')
    if sum%10!=0:
        return False
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=2:
            return False
    return True
def main():
    t=int(input())
    for j in range(t):
        s=input()
        if check(s):
            print("YES")
        else:
            print("NO")
        
if __name__=="__main__":
    main()