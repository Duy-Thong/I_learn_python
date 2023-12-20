n, m = map(int, input().split())
votes = list(map(int, input().split()))
vote_counts = [votes.count(i) for i in range(1, m + 1)]
sorted_counts = sorted(vote_counts)
second_highest_count = sorted_counts[-2]
if vote_counts.count(second_highest_count) == 1:
    winner = vote_counts.index(second_highest_count) + 1
    print(winner)
else:
    print("NONE")
