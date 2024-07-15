from itertools import product

def generate_ternary_numbers(num):
    n = 1
    result = []
    while len(result) < num:
        for p in product('012', repeat=n):
            if p.count('2') > n / 2:
                result.append(''.join(p))
                if len(result) == num:
                    break
        n += 1
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    res = generate_ternary_numbers(n)
    print(' '.join(res))
