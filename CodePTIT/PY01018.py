def encode_decode_reverse(K, S, P):
    encoded_str = ""
    for char in S:
        index = P.index(char)
        encoded_index = (index + K) % 28
        encoded_str += P[encoded_index]
    return encoded_str[::-1]

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    T=input()
    if T=="0":
        break
    else:
        K, S = T.split()
        K = int(K)
        if K == 0:
            break
        encoded_result = encode_decode_reverse(K, S, P)
        print(encoded_result)
