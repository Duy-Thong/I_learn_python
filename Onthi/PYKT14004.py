def main():
    matrix = []
    while True:
        try:
            line = input()
            if not line:
                break
            else:
                row = list(map(int, line.split()))
                matrix.append(row)
        except EOFError:
            break

    a = sorted(matrix[0])
    b = sorted(matrix[1], reverse=True)
    c = sorted(matrix[2])

    res = [a[i] + b[i] + c[i] for i in range(4)]

    # Calculate the minimum difference
    min_difference = min(res[i + 1] - res[i] for i in range(3))

    print(min_difference)

if __name__ == "__main__":
    main()
