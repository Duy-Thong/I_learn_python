import re

n = int(input())
s = ''
for _ in range(n):
    s+=" "
    s += input()

words = re.findall(r'\b\w+\b', s)
words = [word.lower() for word in words]

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word,count)
