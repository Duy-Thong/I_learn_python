def calculate_play_time(start, end):
    start_hours, start_minutes = map(int, start.split(':'))
    end_hours, end_minutes = map(int, end.split(':'))
    return (end_hours * 60 + end_minutes) - (start_hours * 60 + start_minutes)

def main():
    n = int(input())
    players = []
    for _ in range(n):
        player_id = input().strip()
        player_name = input().strip()
        start_time = input().strip()
        end_time = input().strip()
        play_time = calculate_play_time(start_time, end_time)
        players.append((player_id, player_name, play_time))
    
    players.sort(key=lambda x: x[2], reverse=True)
    
    for player in players:
        print(f'{player[0]} {player[1]}  {player[2]//60} gio {player[2]%60} phut')

if __name__ == "__main__":
    main()
