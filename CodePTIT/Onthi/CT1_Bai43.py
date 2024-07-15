def count(N, D, schedules):
    max_free_days = 0  
    current_free_days = 0  
    for day in range(D):
        is_free_day = all(schedule[day] == 'o' for schedule in schedules)
        if is_free_day:
            current_free_days += 1
            max_free_days = max(max_free_days, current_free_days)
        else:
            current_free_days = 0
    return max_free_days

N, D = map(int, input().split())
schedules = [input().strip() for _ in range(N)]
result = count(N, D, schedules)
print(result)
