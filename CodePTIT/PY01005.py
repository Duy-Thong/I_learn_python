def check(s):
    l = len(s)
    cnt4, cnt7 = 0, 0
    for i in range(l):
        if s[i] == '4':
            cnt4 += 1
        if s[i] == '7':
            cnt7 += 1
    if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
        return True
    else:
        return False

def main():
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
