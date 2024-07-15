n = int(input())
data = []
for i in range(n):
    data.append(input())

ds = {}
current_topic = ''

for i in range(n):
    if i == 0 or data[i - 1] == '':
        current_topic = data[i]
        ds[current_topic] = 0
    elif data[i] != '':
        ds[current_topic] += 1

for i in ds:
    print(f'{i}: {ds[i]}')
