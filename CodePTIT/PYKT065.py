def count_numbers(L, R, N):
    count = 0
    for i in range(L, R + 1):
        divisible = False
        for j in range(2, N + 1):
            if i % j == 0:
                divisible = True
                break
        if not divisible:
            count += 1
    return count

while True:
    s=input()
    if len(s.split()) == 1:
        break
    L, R = map(int, s.split())
    N = int(input())
    print(count_numbers(L, R, N))
