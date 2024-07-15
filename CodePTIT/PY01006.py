def check(s):
    l=len(s)
    for i in range(l):
        if s[i]!='4' and s[i]!='7':
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