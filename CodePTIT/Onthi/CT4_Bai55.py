from datetime import datetime, timedelta

class Athlete:
    def __init__(self, code, name, birth_date, start_time, end_time):
        self.code = code
        self.name = name
        self.birth_date = birth_date
        self.start_time = start_time
        self.end_time = end_time
        self.calculate_attributes()

    def calculate_attributes(self):
        age = 2021 - self.birth_date.year
        self.priority = self.calculate_priority(age)
        self.actual_time = self.calculate_actual_time(self.start_time, self.end_time)
        self.rank_time = self.actual_time - self.priority

    @staticmethod
    def calculate_priority(age):
        if age < 18:
            return timedelta()
        elif 18 <= age < 25:
            return timedelta(seconds=1)
        elif 25 <= age < 32:
            return timedelta(seconds=2)
        else:
            return timedelta(seconds=3)

    @staticmethod
    def calculate_actual_time(start_time, end_time):
        start_datetime = datetime.strptime(start_time, '%H:%M:%S')
        end_datetime = datetime.strptime(end_time, '%H:%M:%S')
        return end_datetime - start_datetime

def format_timedelta(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def main():
    n = int(input())
    athletes = []

    for i in range(1, n + 1):
        name = input().title()
        birth_date = datetime.strptime(input(), '%d/%m/%Y')
        start_time = input()
        end_time = input()
        if i<10:
            id = 'VDV0'+str(i)
        else:
            id = 'VDV'+str(i)
        athlete = Athlete(id, name, birth_date, start_time, end_time)
        athletes.append(athlete)

    athletes.sort(key=lambda x: (x.rank_time, x.code))
    rank = 0
    currentrank = 0
    previous_ranktime = timedelta()

    for i, athlete in enumerate(athletes, 1):
        if i == 1:
            rank = 1
            currentrank = 1
            previous_ranktime = athlete.rank_time
        elif athlete.rank_time == previous_ranktime:
            rank = currentrank
        else:
            rank = currentrank + 1
            currentrank = rank
            previous_ranktime = athlete.rank_time

        actual_time_str = format_timedelta(athlete.actual_time)
        priority_str = format_timedelta(athlete.priority)
        rank_time_str = format_timedelta(athlete.rank_time)

        print("{} {} {} {} {} {}".format(athlete.code, athlete.name, actual_time_str, priority_str, rank_time_str, rank))

if __name__ == "__main__":
    main()
