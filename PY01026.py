n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    print(f'Test {i+1}:', "YES" if s1 == s2 else "NO")
