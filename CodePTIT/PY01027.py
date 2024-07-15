import re

def is_beautiful_lucky_number(n):
    n = str(n)
    if not all(char in '68' for char in n):
        return "NO"
            
    if re.fullmatch('(6|68|688)*', n):
        return "YES"
    
    return "NO"

n = input()
print(is_beautiful_lucky_number(n))
