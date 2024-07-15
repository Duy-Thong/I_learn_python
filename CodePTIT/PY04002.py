class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def is_valid(self):
        return self.length > 0 and self.width > 0

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def print_info(self):
        if self.is_valid():
            print(self.perimeter(), self.area(), self.color.title())
        else:
            print("INVALID")

length, width, color = input().split()
length = int(length)
width = int(width)
rectangle = Rectangle(length, width, color)
rectangle.print_info()
