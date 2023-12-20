def format_string(s):
    words = s.split()
    formatted_s = ''.join(word[0].upper() + word[1:] for word in words)
    return formatted_s

s = input()

result = format_string(s)
print(result)
