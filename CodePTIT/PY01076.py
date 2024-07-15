import math

def find_gcd(a, b):
    return math.gcd(a, b)

def main():
    T = int(input())
    for _ in range(T):
        a = int(input())
        b = int(input())
        print(find_gcd(a, b))


if __name__ == "__main__":
    main()
