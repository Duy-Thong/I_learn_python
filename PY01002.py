def is_valid_operation(operation):
    if len(operation) != 9:
        return False
    a = int(operation[0])
    b = int(operation[4])
    c = int(operation[8])
    
    return a + b == c

operation = input().strip()
if is_valid_operation(operation):
    print("YES")
else:
    print("NO")
