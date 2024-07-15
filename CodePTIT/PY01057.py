def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
T = int(input())
for _ in range(T):
    N = input()
    
    is_valid = True

    for i in range(0, len(N)):
        if (is_prime(i) and not is_prime(int(N[i]))) or (not is_prime(i) and is_prime(int(N[i]))):
            is_valid = False
            break
        

    if is_valid:
        print("YES")
    else:
        print("NO")