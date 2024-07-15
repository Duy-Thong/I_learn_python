import math
class Student:
    def __init__(self, code, name, scores):
        self.code = code
        self.name = name
        self.scores = scores
        self.average = self.calculate_average()

    def calculate_average(self):
        weights = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        res = sum(a*b for a,b in zip(self.scores, weights)) / sum(weights)
        return math.ceil(res * 10) / 10

    def rank(self):
        if self.average >= 9:
            return 'XUAT SAC'
        elif self.average >= 8:
            return 'GIOI'
        elif self.average >= 7:
            return 'KHA'
        elif self.average >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __lt__(self, other):
        if self.average == other.average:
            return self.code < other.code
        return self.average > other.average

n = int(input())
students = []
for i in range(n):
    name = input().strip()
    scores = list(map(float, input().split()))
    students.append(Student(f"HS{str(i+1).zfill(2)}", name, scores))

students.sort()

for student in students:
    print(f"{student.code} {student.name} {student.average:.1f} {student.rank()}")
