import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

def is_coprime_triple(a, b, c):
    return is_coprime(a, b) and is_coprime(b, c) and is_coprime(a, c)

def main():
    L, R = map(int, input().split())
    triples = []
    for a in range(L, R + 1):
        for b in range(a + 1, R + 1):
            for c in range(b + 1, R + 1):
                if is_coprime_triple(a, b, c):
                    triples.append((a, b, c))
    triples.sort()
    for a, b, c in triples:
        print("("+str(a)+", " +str(b) +", " +str(c)+")")

if __name__ == "__main__":
    main()
