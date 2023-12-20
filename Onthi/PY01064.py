def find_char_at_k(N, K):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_string = "A"
    for i in range(1, N):
        current_string = current_string + alphabet[i] + current_string
    return current_string[K - 1]
def main():
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())
        result = find_char_at_k(N, K)
        print(result)

if __name__ == "__main__":
    main()
