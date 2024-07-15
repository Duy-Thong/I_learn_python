import datetime

class Player:
    def __init__(self, id, name, start, end):
        self.id = id
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        duration = self.end - self.start
        hours, remainder = divmod(duration.seconds, 3600)
        minutes = remainder // 60
        return f"{self.id} {self.name} {hours} gio {minutes} phut"

    def __lt__(self, other):
        return (self.end - self.start) > (other.end - other.start)

def main():
    n = int(input())
    players = []
    for _ in range(n):
        id_input = input()
        name_input = input()
        start_input = datetime.datetime.strptime(input(), '%H:%M')
        end_input = datetime.datetime.strptime(input(), '%H:%M')
        players.append(Player(id=id_input, name=name_input, start=start_input, end=end_input))

    players = sorted(players)
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
