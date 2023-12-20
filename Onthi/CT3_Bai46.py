def count_features(N, Q, features, questions):
    result = []
    
    # Tạo một mảng prefix_sum để lưu trữ tổng số lượng các tính năng từ 1 đến i
    prefix_sum = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + features[i-1]
    
    for q in questions:
        a, b = q
        count_1 = prefix_sum[b] - prefix_sum[a-1]
        count_2 = features[a:b+1].count(2)
        count_3 = features[a:b+1].count(3)
        result.append((count_1, count_2, count_3))
    
    return result

# Example usage
N, Q = map(int, input().split())
features = []
for _ in range(N):
    features.append(int(input()))
questions = []
for _ in range(Q):
    questions.append(tuple(map(int, input().split())))

result = count_features(N, Q, features, questions)
for r in result:
    print(*r)
