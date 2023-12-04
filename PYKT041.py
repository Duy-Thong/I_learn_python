def count_coin_pairs(n, grid):
    row_counts = [0]*n
    col_counts = [0]*n
    total_pairs = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                row_counts[i] += 1
                col_counts[j] += 1
    for count in row_counts + col_counts:
        total_pairs += count * (count - 1) // 2
    
    return total_pairs

n = int(input())
grid = [list(input()) for _ in range(n)]

coin_pairs = count_coin_pairs(n, grid)

print(coin_pairs)
