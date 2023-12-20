from datetime import datetime

class Player:
    def __init__(self, name, team, dob, hgh, pos) -> None:
        s = pos.split()
        self.id = ""
        for i in s:
            self.id += i[0].upper()
        self.name = name
        self.team = team
        self.dob = datetime.strptime(dob, "%d/%m/%Y")
        self.age = (datetime.today() - 
                    datetime.strptime(dob, "%d/%m/%Y")).days
        self.hgh = hgh
        self.pos = pos
    def __str__(self) -> str:
        s = str(datetime.strftime(self.dob, "%d/%m/%Y"))
        return self.id + " " + self.name + " " + self.team + " " + s + " " + str(self.hgh) + " " + self.pos
    

a = []
for i in range(int(input())):
    a.append(Player(input(), input(), input(), int(input()), input()))
a.sort(key=lambda x : (x.age, x.hgh))
a[0].id += str(1)
for i in range(1, len(a)):
    cnt = 1
    for j in range(0, i):
        if a[i].pos == a[j].pos: cnt += 1
    a[i].id += str(cnt)
for i in a:
    print(i)
        