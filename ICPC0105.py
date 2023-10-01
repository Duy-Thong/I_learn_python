import re

T = int(input())
for _ in range(T):
    s = input()
    numbers = re.findall(r'\d+', s)
    min_num = max(map(int, numbers))
    print(min_num)