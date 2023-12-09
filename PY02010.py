while True:
    N = int(input())
    if N == 0:
        break

    numbers = []
    for _ in range(N):
        numbers.append(int(input()))

    if len(set(numbers)) == 1:
        print("BANG NHAU")
    else:
        print(min(numbers), max(numbers))
