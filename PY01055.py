T = int(input())

for _ in range(T):
    N = input()
    
    if len(N) % 2 == 0 or N[0] == N[1]:
        print("NO")
    else:
        first_digit = N[0]
        second_digit = N[1]
        odd_digits = N[0::2]
        
        if first_digit != second_digit and all(digit == first_digit for digit in odd_digits):
            print("YES")
        else:
            print("NO")