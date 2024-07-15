import string

def base_conversion(n, b):
    chars = string.digits + string.ascii_uppercase
    result = ''
    while n > 0:
        n, r = divmod(n, b)
        result = chars[r] + result
    return result

t = int(input())
for _ in range(t):
    N, b = map(int, input().split())
    print(base_conversion(N, b))
