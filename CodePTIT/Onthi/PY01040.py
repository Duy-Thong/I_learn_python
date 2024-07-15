def rotate(s):
    value = sum(ord(c) - ord('A') for c in s) % 26
    rotated_characters = [chr((ord(x) - ord('A') + value) % 26 + ord('A')) for x in s]
    return ''.join(rotated_characters)

def merge(s1, s2):
    merged_string = ""
    for i in range(len(s1)):
        x = (ord(s2[i]) - ord('A') + ord(s1[i]) - ord('A')) % 26 + ord('A')
        merged_string += chr(x)
    return merged_string

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        l = len(s)
        s1 = s[:l // 2]
        s2 = s[l // 2:]

        s1 = rotate(s1)
        s2 = rotate(s2)
        result = merge(s1, s2)
        print(result)

if __name__ == "__main__":
    main()
