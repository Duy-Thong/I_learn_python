class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self, a, b):
        while(b):
            a, b = b, a % b
        return a

    def simplify(self):
        gcd_value = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value

    def display(self):
        print("{}/{}".format(self.numerator, self.denominator))
    def sum(self, a, b):
        self.numerator = a.numerator * b.denominator + b.numerator * a.denominator
        self.denominator = a.denominator * b.denominator
        self.simplify()

numerator, denominator = map(int, input().split())
fraction = Fraction(numerator, denominator)
fraction.simplify()
fraction.display()
