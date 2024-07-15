def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def min_steps_to_prime(n, array):
    steps = 0

    for num in array:
        if not is_prime(num):
            # Tăng hoặc giảm giá trị cho đến khi trở thành số nguyên tố
            for i in range(1, num):
                if is_prime(num + i):
                    num += i
                    break
                elif is_prime(num - i):
                    num -= i
                    break
            steps += 1

    return steps

# Đọc dữ liệu từ input
n = int(input())
arr = list(map(int, input().split()))

# Tính số bước cần thiết
result = min_steps_to_prime(n, arr)

# In kết quả
print(result)
