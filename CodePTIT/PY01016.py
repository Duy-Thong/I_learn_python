def decode(encoded_str):
    decoded_str = ""
    i = 0
    while i < len(encoded_str):
        char = encoded_str[i]
        count = int(encoded_str[i+1])
        decoded_str += char * count
        i += 2
    return decoded_str
num_tests = int(input())
for _ in range(num_tests):
    encoded_str = input().strip()
    decoded_str = decode(encoded_str)
    print(decoded_str)
