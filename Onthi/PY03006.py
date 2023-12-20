import re

n = int(input())
s = ""
for _ in range(n):
    s += " " + input().lower()

s1 = re.findall(r'[a-zA-Z]+', s)
res = {}
for i in s1:
    res[i] = 0
for i in s1:
    res[i] += 1

sorted_res = sorted(res.items(), key=lambda x: (-x[1], x[0]))

for item in sorted_res:
    print(item[0], item[1])
