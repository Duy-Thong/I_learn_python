def transform_matrix(N, M, matrix):
    if N > M:
        # Loại bỏ các hàng có thứ tự lẻ
        matrix = [matrix[i] for i in range(N) if i % 2 == 0]
        N = len(matrix)
    elif M > N:
        # Loại bỏ các cột có thứ tự chẵn
        matrix = [row[1::2] for row in matrix]
        M = len(matrix[0])

    return matrix

def main():
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    result_matrix = transform_matrix(N, M, matrix)

    for row in result_matrix:
        print(*row)

if __name__ == "__main__":
    main()
