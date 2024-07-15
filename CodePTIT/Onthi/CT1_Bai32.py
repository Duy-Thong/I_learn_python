import datetime
class Gamer:
    def __init__(self,username,password,user,timein,timeout):
        self.username = username
        self.password = password
        self.user = user
        self.timein = timein
        self.timeout = timeout
        self.playtime = timeout - timein
    def __lt__(self, other):
        if self.playtime == other.playtime:
            return self.user > other.user
        return self.playtime > other.playtime
    def __str__(self):
        hours, remainder = divmod(self.playtime.seconds, 3600)
        minutes = remainder // 60
        return f"{self.username} {self.password} {self.user} {hours} gio {minutes} phut"
def main():
    t=int(input())
    list=[]
    for i in range(t):
        username= input()
        password= input()
        user= input()
        timein= datetime.datetime.strptime(input(), '%H:%M')
        timeout= datetime.datetime.strptime(input(), '%H:%M')
        list.append(Gamer(username,password,user,timein,timeout))
    list.sort()
    for i in list:
        print(i)

if __name__ == '__main__':
    main()