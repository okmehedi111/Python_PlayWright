#OOP
class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print(f"Area: {0.5 * self.base * self.height}")
T1 = Triangle(10,20)
T1.area()
T2 = Triangle(20,30)
T2.area()