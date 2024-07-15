def process_strings():
    str1 = input().lower().split()
    str2 = input().lower().split()

    set1 = set(str1)
    set2 = set(str2)

    union_set = set1.union(set2)
    intersect_set = set1.intersection(set2)

    union_list = sorted(list(union_set))
    intersect_list = sorted(list(intersect_set))

    union_str = ' '.join(union_list)
    intersect_str = ' '.join(intersect_list)
    print(union_str)
    print(intersect_str)

process_strings()
