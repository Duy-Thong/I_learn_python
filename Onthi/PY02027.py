import re
def main():
    a=[]
    t=int(input())
    for _ in range(t):
        s=input()
        tmp = re.findall("\d+",s)
        for i in tmp:
            a.append(int(i))
    a=sorted(a)
    for i in a:
        print(i)
if __name__=="__main__":
    main()
