def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=set(a)
    b=set(b)
    c=sorted(a.intersection(b))
    print(*c)
    c=sorted(a.difference(b))
    print(*c)
    c=sorted(b.difference(a))
    print(*c)
if __name__=="__main__":
    main()