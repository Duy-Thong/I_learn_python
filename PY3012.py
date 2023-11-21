class Student:
    def __init__(self, name, correct, submits):
        self.name = name
        self.correct = correct
        self.submits = submits

    def __lt__(self, other):
        if self.correct != other.correct:
            return self.correct > other.correct
        if self.submits != other.submits:
            return self.submits < other.submits
        return self.name < other.name

def ranking_students():
    N = int(input())
    students = []

    for _ in range(N):
        name = input()
        correct, submits = map(int, input().split())
        students.append(Student(name, correct, submits))

    students.sort()

    for student in students:
        print(student.name + " " + str(student.correct)+ " " + str(student.submits))

ranking_students()
