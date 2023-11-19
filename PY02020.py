N = int(input())
scores = list(map(float, input().split()))

min_score = min(scores)
max_score = max(scores)

scores = [score for score in scores if score != min_score and score != max_score]

avg_score = sum(scores) / len(scores)

print("{:.2f}".format(avg_score))
