# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:09:20 2024

@author: Fairuz Maulidya
"""

from shapes import Square, Triangle, Circle, Rectangle, Parallelogram

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
