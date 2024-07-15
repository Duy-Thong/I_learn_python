def sum_of_digits(n):
    return sum(map(int, str(n)))

def sort_array(arr):
    # Sort array based on sum of digits
    # If sum of digits is equal, sort based on value
    arr.sort(key=lambda x: (sum_of_digits(x), x))
    return arr

# Input number of test cases
t = int(input())
for _ in range(t):
    # Input size of array
    n = int(input())
    # Input elements of array
    arr = list(map(int, input().split()))
    # Sort array as per the given conditions
    sorted_arr = sort_array(arr)
    # Print sorted array
    for num in sorted_arr:
        print(num, end=" ")
    print()
