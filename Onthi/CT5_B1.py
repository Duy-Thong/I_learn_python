def convert_time(h, m, a, b):
    new_hour = (h + (b - a)) % 24
    new_minute = m
    return new_hour, new_minute
h, m, a, b = list(map(int, input().split()))
new_h, new_m = convert_time(h, m, a, b)
print(new_h, new_m)
