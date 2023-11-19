def is_balanced(s):
    reversed_s = s[::-1]  # reverse the string
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(reversed_s[i]) - ord(reversed_s[i - 1])):
            return "NO"
    return "YES"

# Test
t = int(input())
for _ in range(t):
    s = input().strip()
    print(is_balanced(s))
