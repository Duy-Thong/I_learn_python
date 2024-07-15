import datetime

class Movie:
    def __init__(self, id, name, day, cnt, movie_type):
        self.id = id
        self.name = name
        self.day = day
        self.cnt = cnt
        self.type = movie_type

    def __str__(self):
        formatted_date = self.day.strftime("%d/%m/%Y")
        return f"{self.id} {self.type} {formatted_date} {self.name} {self.cnt}"

    def __lt__(self, other):
        if self.day != other.day:
            return self.day < other.day
        elif self.name != other.name:
            return self.name < other.name
        else:
            return self.cnt > other.cnt

def main():
    n, m = map(int, input().split())
    theloai = {}

    for i in range(n):
        theloai[i + 1] = input()

    phim = []
    for i in range(m):
        id = "P{:03d}".format(i + 1)

        tmp = input()
        tl = theloai[int(tmp[4])]
        day = datetime.datetime.strptime(input(), "%d/%m/%Y").date()
        name = input()
        num = int(input())
        phim.append(Movie(id, name, day, num, tl))

    phim = sorted(phim)
    for mv in phim:
        print(mv)

if __name__ == "__main__":
    main()
