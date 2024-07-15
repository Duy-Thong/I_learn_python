class Vehicle:
    def __init__(self, plate, type, seats, direction, date):
        self.plate = plate
        self.type = type
        self.seats = seats
        self.direction = direction
        self.date = date

def calculate_fee(vehicles):
    fee_table = {
        ('Xe_con', 5): 10000,
        ('Xe_con', 7): 15000,
        ('Xe_tai', 2): 20000,
        ('Xe_khach', 29): 50000,
        ('Xe_khach', 45): 70000
    }
    date_fee = {}
    for vehicle in vehicles:
        if vehicle.direction == 'IN':
            fee = fee_table.get((vehicle.type, vehicle.seats), 0)
            if vehicle.date in date_fee:
                date_fee[vehicle.date] += fee
            else:
                date_fee[vehicle.date] = fee
    for date, fee in date_fee.items():
        print(f"{date}: {fee}")

N = int(input())
vehicles = []
for _ in range(N):
    plate, type, seats, direction, date = input().split()
    seats = int(seats)
    vehicles.append(Vehicle(plate, type, seats, direction, date))

calculate_fee(vehicles)
