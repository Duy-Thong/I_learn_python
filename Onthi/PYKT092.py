class ThiSinh:
    num_ts = 1
    def __init__(self, hoten, diem, dantoc, khuvuc):
        self.ma = "TS" + str(ThiSinh.num_ts).zfill(2)
        ThiSinh.num_ts += 1
        self.hoten = hoten
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc

    def tinh_tong_diem(self):
        tong_diem = self.diem
        if self.khuvuc == 1:
            tong_diem += 1.5
        elif self.khuvuc == 2:
            tong_diem += 1
        if self.dantoc != "Kinh":
            tong_diem += 1.5
        return round(tong_diem, 1)

    def trang_thai_trung_tuyen(self, diem_chuan):
        return "Do" if self.tinh_tong_diem() >= diem_chuan else "Truot"
def chuan_hoa_ten(hoten):
    return ' '.join(word.capitalize() for word in hoten.split())
n = int(input())
danh_sach_ts = []
for i in range(n):
    hoten = input().strip()
    diem = float(input())
    dantoc = input().strip()
    khuvuc = int(input())
    ts = ThiSinh(chuan_hoa_ten(hoten), diem, dantoc, khuvuc)
    danh_sach_ts.append(ts)
diem_chuan = 20.5
danh_sach_ts.sort(key=lambda x: (-x.tinh_tong_diem(), x.ma))
for ts in danh_sach_ts:
    print(f"{ts.ma} {ts.hoten} {ts.tinh_tong_diem()} {ts.trang_thai_trung_tuyen(diem_chuan)}")
