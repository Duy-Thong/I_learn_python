def number_parentheses(expression):
    stack = []
    result = []
    count = 0

    for char in expression:
        if char == '(':
            count += 1
            stack.append(count)
            result.append(count)
        elif char == ')':
            result.append(stack.pop())
        else:
            result.append(0)

    return result

def main():
    t = int(input())
    for _ in range(t):
        expression = input().strip()
        result = number_parentheses(expression)
        res = [x for x in result if x != 0]
        
        print(*res)

if __name__ == "__main__":
    main()
