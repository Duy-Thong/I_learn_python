def chuyenvi(l):
    l1 = list(zip(*l))
    return l1
def multiply_matrices(l1, l2):
    n = len(l1)
    m = len(l1[0])
    for i in range(n):
        for j in range (n):
            sum=0
            for k in range (0,m):
                sum += l1[i][k]*l2[k][j]
            print(sum , end=" ")
        print()
def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        l = []
        for _ in range(n):
            row = list(map(int, input().split()))
            l.append(row)
        l2 = chuyenvi(l)
        multiply_matrices(l, l2)

if __name__ == "__main__":
    main()
