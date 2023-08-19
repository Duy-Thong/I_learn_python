def transform_string(s):
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())
    
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()

def main():
    s = input()
    result = transform_string(s)
    print(result)

if __name__ == "__main__":
    main()
