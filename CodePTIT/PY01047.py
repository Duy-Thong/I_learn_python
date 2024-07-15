def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def check(s):
    num=s[len(s)-4:]
    num=int(num)
    if is_prime(num):
        print("YES")
    else:
        print("NO")
t=int(input())
for _ in range(t):
    s=input()
    check(s)

