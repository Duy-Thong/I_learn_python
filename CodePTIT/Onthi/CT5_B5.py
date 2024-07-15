from datetime import datetime

class Cauthu:
    def __init__(self, ma, ten, tendoi, ngaysinh, chieucao, vitri):
        self.ma = ma
        self.ten = ten
        self.tendoi = tendoi
        self.ngaysinh = ngaysinh
        self.chieucao = chieucao
        self.vitri = vitri

    def __lt__(self, other):
        if self.ngaysinh != other.ngaysinh:
            return self.ngaysinh > other.ngaysinh
        else:
            return self.chieucao < other.chieucao

    def __str__(self):
        formated_date = self.ngaysinh.strftime("%d/%m/%Y")
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.tendoi, formated_date, self.chieucao, self.vitri)

def chuanhoangaysinh(s):
    words = s.split("/")
    if len(words[0]) < 2:
        words[0] = "0" + words[0]
    if len(words[1]) < 2:
        words[1] = "0" + words[1]
    return words[0] + "/" + words[1] + "/" + words[2]

def main():
    t = int(input())
    ds = []
    dsvt = {}
    for i in range(t):
        ten = input().strip()
        tendoi = input()
        ngaysinh = datetime.strptime(chuanhoangaysinh(input()), "%d/%m/%Y")
        chieucao = int(input())
        vitri = input()
        vt = "".join(s[0] for s in vitri.split())
        
        if vt not in dsvt:
            dsvt[vt] = 1
        else:
            dsvt[vt] += 1
        
        cnt = dsvt[vt]
        
        if cnt < 10:
            ma = vt + "0" + str(cnt)
        else:
            ma = vt + str(cnt)
        
        ds.append(Cauthu(ma, ten, tendoi, ngaysinh, chieucao, vitri))
    
    ds.sort()
    
    for i in ds:
        print(i)

if __name__ == "__main__":
    main()
