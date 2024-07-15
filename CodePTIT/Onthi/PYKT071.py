def read_binary_file(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return list(map(int, binary_data.split()))

def find_non_decreasing_numbers(data1, data2):
    result = []
    count_data1 = {}
    count_data2 = {}

    for num in data1:
        count_data1[num] = count_data1.get(num, 0) + 1

    for num in data2:
        count_data2[num] = count_data2.get(num, 0) + 1

    common_numbers = set(data1) & set(data2)

    for num in sorted(common_numbers):
        result.append((num, count_data1.get(num, 0), count_data2.get(num, 0)))

    return result

def main():
    data1 = read_binary_file('DATA1.in')
    data2 = read_binary_file('DATA2.in')

    result = find_non_decreasing_numbers(data1, data2)

    for item in result:
        print(f'{item[0]} {item[1]} {item[2]}')

if __name__ == "__main__":
    main()
