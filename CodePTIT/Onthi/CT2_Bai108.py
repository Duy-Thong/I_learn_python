# Định nghĩa hàm happiness với tham số là số ngày (n) và ma trận điểm vui vẻ từ các hoạt động (a)
def happiness(n, a):
    # Khởi tạo ma trận dp với n hàng và 4 cột, tất cả giá trị ban đầu là 0
    dp = [[0] * 4 for _ in range(n)]

    # Duyệt qua từng ngày
    for i in range(n):
        # Duyệt qua từng loại hoạt động (A, B, C, D)
        for j in range(4):
            # Cập nhật giá trị tại dp[i][j] bằng cách lấy giá trị lớn nhất
            # giữa giá trị tại hoạt động j của ngày i và giá trị lớn nhất
            # của các hoạt động của ngày trước đó mà không giống với hoạt động j
            dp[i][j] = max(dp[i][j], a[i][j] + max(dp[i - 1][:j] + dp[i - 1][j + 1:]))

    # Trả về giá trị lớn nhất của hàng cuối cùng của ma trận dp
    return max(dp[-1])

# Nhập số ngày n
n = int(input())

# Nhập ma trận điểm vui vẻ từ các hoạt động cho mỗi ngày
a = [list(map(int, input().split())) for _ in range(n)]

# Gọi hàm happiness và lưu kết quả vào biến result
result = happiness(n, a)

# In ra kết quả là tổng điểm vui vẻ tối đa mà Đức có thể đạt được
print(result)
