def min_sum_triplet(arr, n):
    # Initialize the minimum sum to a very high value
    min_sum = float('inf')
    # Check all possible triplets in the array
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Update min_sum if the current triplet sum is less
                min_sum = min(min_sum, arr[i] + arr[j] + arr[k])
    return min_sum

# Main code to process input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_sum_triplet(arr, n))
