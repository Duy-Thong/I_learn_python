def sort_and_sum(S):
    letters = [c for c in S if c.isalpha()]
    digits = [int(c) for c in S if c.isdigit()]

    letters.sort()
    sum_digits = sum(digits)

    return ''.join(letters) + str(sum_digits)


T = int(input())
for _ in range(T):
    S = input()
    print(sort_and_sum(S))
