def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def is_head_tail_prime(n):
    head = int(n[:3])
    tail = int(n[-3:])
    return is_prime(head) and is_prime(tail)


def main():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        if is_head_tail_prime(n):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
