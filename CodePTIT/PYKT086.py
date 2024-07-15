def binary_to_base(binary_str, base):
    if base not in (2, 4, 8, 16):
        raise ValueError("Base must be one of [2, 4, 8, 16]")
    base_conversion = {2: 1, 4: 2, 8: 3, 16: 4}
    chunk_size = base_conversion[base]
    decimal_number = int(binary_str, 2)
    if base == 2:
        return binary_str
    else:
        return format(decimal_number, 'o') if base == 8 else format(decimal_number, 'x')

with open('DATA.in', 'r') as file:
    t = int(file.readline())
    for _ in range(t):
        b = int(file.readline().strip())
        binary_str = file.readline().strip()
        print(binary_to_base(binary_str, b))
