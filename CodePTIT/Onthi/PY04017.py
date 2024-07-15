import datetime

class CuaRo:
    def __init__(self, ho_ten, don_vi, thoi_diem):
        self.ho_ten = ho_ten
        self.don_vi = don_vi
        self.thoi_diem = thoi_diem
        self.ma = self.generate_ma()
        self.vantoc = self.get_vantoc()

    def generate_ma(self):
        ho_ten_parts = self.ho_ten.split()
        don_vi_parts = self.don_vi.split()
        ma = ''.join([part[0].lower() for part in don_vi_parts + ho_ten_parts])
        return ma.upper()

    def get_vantoc(self):
        start = datetime.datetime.strptime("6:00", "%H:%M")
        time_difference = (self.thoi_diem - start).total_seconds()/3.6 
        speed = 120000 / time_difference
        return round(speed)

def main():
    so_luong_cua_ro = int(input())
    danh_sach_cua_ro = []

    for _ in range(so_luong_cua_ro):
        ho_ten = input()
        don_vi = input()
        thoi_diem_str = input()
        thoi_diem = datetime.datetime.strptime(thoi_diem_str, "%H:%M")
        danh_sach_cua_ro.append(CuaRo(ho_ten, don_vi, thoi_diem))

    danh_sach_cua_ro.sort(key=lambda x: x.thoi_diem)

    for cua_ro in danh_sach_cua_ro:
        print(f"{cua_ro.ma} {cua_ro.ho_ten} {cua_ro.don_vi} {cua_ro.vantoc} Km/h")

if __name__ == "__main__":
    main()
