def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    t = int(input())
    for j in range(t):
        n = int(input())
        count = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                count += 1
        if is_prime(count):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
