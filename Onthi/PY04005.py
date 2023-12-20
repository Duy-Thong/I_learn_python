import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        return self.p1.distance(self.p2) + self.p1.distance(self.p3) + self.p2.distance(self.p3)
    def check(self):
        a=self.p1.distance(self.p2)
        b=self.p1.distance(self.p3)
        c=self.p2.distance(self.p3)
        if a+b<=c or a+c<=b or b+c<=a:
            return False
        else:
            return True
def main():
    t=int(input())
    for _ in range(t):
        a=list(map(int,input().split()))
        p1= Point(a[0],a[1])
        p2= Point(a[2],a[3])
        p3 = Point(a[4],a[5])
        trig = Triangle(p1,p2,p3)
        if trig.check():
            print(f'{trig.perimeter():.3f}')
        else:
            print("INVALID")
if __name__=="__main__":
    main()