import math

class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
  
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)

class Circle:
	def __init__(self, radious):
		self.radious = radious
		
	def getArea(self):
		return (self.radious ** 2) * math.pi
  
	def getPerimeter(self):
		return 2 * math.pi * self.radious