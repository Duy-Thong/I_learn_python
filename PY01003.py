def solve(s):
    i = len(s) - 1
    carrier = 0
    s = list(s)

    while i > 0:
        if int(s[i]) >= 5:
            if s[i] == '9':
                s[i] = '0'
                carrier = 1
            else:
                s[i] = '0'
                s[i - 1] = str(int(s[i - 1]) + 1)
                carrier = 0
        else:
            s[i] = '0'
            carrier = 0
        i -= 1

    if carrier:
        if s[0] == '9':
            s[0] = '0'
            s.insert(0, '1')
        else:
            s[0] = str(int(s[0]) + 1)

    return ''.join(s)

# Đọc số bộ test
num_test_cases = int(input())

# Đọc và xử lý từng bộ test
for _ in range(num_test_cases):
    s = input()
    result = solve(s)
    print(result)
