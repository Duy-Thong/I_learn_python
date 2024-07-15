def insert_commas(s):
    start = len(s) % 3
    s_with_commas = s[:start] + ',' + ','.join(s[i:i+3] for i in range(start, len(s), 3))
    if s_with_commas[0]==',':
        s_with_commas = s_with_commas[1:]
    return s_with_commas
n =input()
if(len(n)<3):
    print(n)
else:
    print(insert_commas(n))
