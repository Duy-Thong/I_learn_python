def encode(s):
    l = len(s)
    res = ""
    i = 0
    while i < l:
        count = 1
        while i < l - 1 and s[i] == s[i + 1]:
            i += 1
            count += 1
        res += str(count) + s[i]
        i += 1
    return res


t = int(input())
for _ in range(t):
    s = input()
    print(encode(s))
