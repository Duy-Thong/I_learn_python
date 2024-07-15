from datetime import datetime
from collections import defaultdict

def calculate_average_rainfall(n, rainfall_data):
    stations = defaultdict(lambda: [0, 0])  
    for data in rainfall_data:
        start_time = datetime.strptime(data[1], "%H:%M")
        end_time = datetime.strptime(data[2], "%H:%M")
        duration = (end_time - start_time).total_seconds() / 3600  
        rainfall = data[3]
        stations[data[0]][0] += rainfall
        stations[data[0]][1] += duration

    station_ids = {station: index for index, station in enumerate(stations, start=1)}
    average_rainfalls = []
    for station, (total_rainfall, total_duration) in stations.items():
        average_rainfall = total_rainfall / total_duration
        average_rainfalls.append((f"T{station_ids[station]:02d}", station, "%.2f" % average_rainfall))

    return average_rainfalls

# Example usage:
n = int(input())
rainfall_data = []
for _ in range(n):
    station = input().strip()
    start_time = input().strip()
    end_time = input().strip()
    rainfall = float(input().strip())
    rainfall_data.append((station, start_time, end_time, rainfall))
for average_rainfall in calculate_average_rainfall(n, rainfall_data):
    print(*average_rainfall)