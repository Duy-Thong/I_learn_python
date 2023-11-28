def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

T = int(input())
for _ in range(T):
    ip = input().strip()
    if is_valid_ipv4(ip):
        print("YES")
    else:
        print("NO")
