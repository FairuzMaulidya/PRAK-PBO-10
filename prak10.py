# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:54:40 2024

@author: Fairuz Maulidya
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

# Main program
square = Square(7)
triangle = Triangle(8, 6)
circle = Circle(10)
rectangle = Rectangle(7, 4)
parallelogram = Parallelogram(8, 6)

print('''====================
Nama: Fairuz Maulidya      
Nim: 064002300018          
===================''')
print("Luas Persegi:", square.calculate_area())
print("Luas Segitiga:", triangle.calculate_area())
print("Luas Lingkaran:", circle.calculate_area())
print("Luas Persegi Panjang:", rectangle.calculate_area())
print("Luas Jajar Genjang:", parallelogram.calculate_area())
