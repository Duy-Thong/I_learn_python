from datetime import datetime
class Khachhang:
    gia =[30,45,50,65,72,85,90,120,150]
    def __init__(self,ma,ten,sophong,ngaynhan,ngaytra,dichvu):
        if ma<10:
            self.ma = "KH0"+str(ma)
        else:
            self.ma = "KH"+str(ma)
        self.ten = ten
        self.sophong = sophong
        self.ngaynhan = ngaynhan
        self.ngaytra = ngaytra
        self.songay=(self.ngaytra-self.ngaynhan).days+1
        self.dichvu = dichvu
        songay=(self.ngaytra-self.ngaynhan).days+1
        tang = int(self.sophong[0])
        gia = Khachhang.gia[tang-1]
        self.tong = songay*gia+self.dichvu

    def __lt__(self,other):
        if self.tong == other.tong:
            return (self.ngaytra-self.ngaynhan).days < (other.ngaytra-other.ngaynhan).days
        else:
            return self.tong > other.tong
    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.ten, self.sophong, self.songay, self.tong)
def main():
    t=int(input())
    ds=[]
    for i in range(t):
        ma = i+1
        ten = input()
        sophong = input()
        ngaynhan = datetime.strptime(input(), '%d/%m/%Y')
        ngaytra = datetime.strptime(input(), '%d/%m/%Y')
        dichvu = int(input())
        ds.append(Khachhang(ma,ten,sophong,ngaynhan,ngaytra,dichvu))
    ds.sort()
    for i in ds:
        print(i)
if __name__ == "__main__":
    main()