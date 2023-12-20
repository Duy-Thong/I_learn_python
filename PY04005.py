class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        if self.x == other.x and self.y == other.y:
            return 0
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
def main():
   t=int(input())
   for _ in range(t):
       x1,y1,x2,y2,x3,y3=map(int,input().split())
       p1=Point(x1,y1)
       p2=Point(x2,y2)
       p3=Point(x3,y3)
       d1=p1.distance(p2)
       d2=p1.distance(p3)
       d3=p2.distance(p3)
       if d1+d2<=d3 or d1+d3<=d2 or d2+d3<=d1:
            print("INVALID")
       else:
           perimeter = round(d1 + d2 + d3, 3)
           print(perimeter)
if __name__ == "__main__":
    main()