def solve_hidden_arithmetic(T, test_cases):
    for _ in range(T):
        expr = test_cases[_]
        operators = ["+", "-", "*", "/"]
        results = []
        for op in operators:
            temp_expr = expr.replace('?', '0').replace('??', '0').replace('?', op)
            left, right = temp_expr.split("=")
            try:
                if eval(left) == int(right):
                    results.append(temp_expr.replace('0', '?'))
            except ZeroDivisionError:
                continue
        if len(results) == 1:
            print(results[0])
        else:
            print("WRONG PROBLEM!")

T = 2
test_cases = ["?0 ? 12 = 28", "40 / ?3 = ??"]
solve_hidden_arithmetic(T, test_cases)
