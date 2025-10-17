import math

class Shape:
    def area(self):
        """Base method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with its radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
