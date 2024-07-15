def insert_string_at_position(S1, S2, p):
    return S1[:p-1] + S2 + S1[p-1:]

S1 = input()
S2 = input()
p = int(input())
print(insert_string_at_position(S1, S2, p))  # Expected output: "ngon ngu C.mon thcs2 hoc de"
