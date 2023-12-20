
class Sinhvien:
    def __init__(self, masv, hoten,ngaysinh, diem1,diem2,diem3):
        self.masv = masv
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong_diem = diem1+diem2+diem3
  
    def __lt__(self, other):
        if self.tong_diem == other.tong_diem:
            return self.masv < other.masv
        else:
            return self.tong_diem > other.tong_diem
    def __str__(self):
        return "{} {} {} {:.1f}".format(self.masv, self.hoten, self.ngaysinh, self.tong_diem)
def main():
    n=int(input())
    l=[]
    for i in range(n):
        masv=i+1
        hoten=input()
        ngaysinh=input()
        diem1=float(input())
        diem2=float(input())
        diem3=float(input())
        l.append(Sinhvien(masv,hoten,ngaysinh,diem1,diem2,diem3))
    l.sort()
    for i in l:
        print(i)
if __name__ == "__main__":
    main()