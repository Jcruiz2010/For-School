import math

class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.height * self.base

    def perimeter(self):
        return 2 * (self.height + self.base)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


try:
    while True:
        questionShapes = input("What shape do you want to gather the perimeter and area?\n\n1. Circle\n2. Rectangle\n3. Triangle\n\nType here: ")
        print()
        match(questionShapes):
            case "1":
                radiusCircle = float(input("What is the radius of your circle?\n\nType here: "))
                circle = Circle(radiusCircle)
                print()
                print(f"Area: {circle.area()}")
                print(f"Perimeter: {circle.perimeter()}")

            case "2":
                baseRectangle = float(input("What is the base of the rectangle?\n\nType here: "))
                print()
                heightRectangle = float(input("What is the height of the rectangle?\n\nType here: "))
                rectangle = Rectangle(heightRectangle, baseRectangle)
                print()
                print(f"Area: {rectangle.area()}")
                print(f"Perimeter: {rectangle.perimeter()}")

            case "3":
                firstSide = float(input("What is the first side of the triangle (a)?\n\nType here: "))
                print()
                secondSide = float(input("What is the second side of the triangle (b)?\n\nType here: "))
                print()
                thirdSide = float(input("What is the third side of the triangle (c)?\n\nType here: "))
                triangle = Triangle(firstSide, secondSide, thirdSide)
                print()
                print(f"Area: {triangle.area()}")
                print(f"Perimeter: {triangle.perimeter()}")

except ValueError as e:
    print(f"Something went wrong: You put a letter instead of a number. {e}")


