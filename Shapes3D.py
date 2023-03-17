import math


class Shape:
	def __init__(self):
		raise NotImplementedError()

	def GetArea(self): pass
	def GetPerimeter(self): pass
	def GetVolume(self): pass


class Polygon(Shape):
	def __init__(self, sideLength:float, sides:int):
		''' A representation of a regular polygon defined by sides and side length.

		Maths functions will be pulled from the wiki page:
		https://en.wikipedia.org/wiki/Regular_polygon

		Arguments:
			sideLength(float): The length of the sides. Regular polygons have congruent side lengths. Must be a positive, non-zero number.
			sides(int): The number of sides that the regular polygon will have. Must be a number larger than 2.
		'''
		# Validating side length
		if sideLength <= 0:
			raise ValueError(f'sideLength must by a positive, non-zero number. Received `{sideLength}`.')

		# Validating side count
		if sides < 3:
			raise ValueError(f'side count must be a number larger than 2. Received `{sides}`')

		# Setting member variables now that we've validated input
		self._sideLength = sideLength
		self._sides = sides

	def GetArea(self) -> float:
		''' Gets the area of the regular polygon.

		Returns: A float representing the area of the regular polygon.
		'''
		cotComponent = (
			math.cos(math.pi / self._sides)
			/
			math.sin(math.pi / self._sides)
		)

		return (self._sides / 4) * (self._sideLength ** 2) * cotComponent

	def GetPerimeter(self) -> float:
		''' Gets the perimeter of the regular polygon.

		Returns: A float representing the perimeter of the regular polygon.
		'''
		return self._sideLength * self._sides
	
class Cuboid(Shape):
	def __init__(self, length:float, width:float, height:float):
		self.length = length
		self.width = width
		self.height = height

	def GetArea(self) -> float:
		return 2 * ((self.length * self.width) + (self.width * self.height) + (self.length * self.height))
	
	def GetVolume(self) -> float:
		return self.length * self.width * self.height
	
class Cube(Shape):
	def __init__(self, edge:float):
		self.edge = edge

	def GetArea(self) -> float:
		return 6 * pow(self.edge, 2)
	
	def GetVolume(self) -> float:
		return 6 * pow(self.edge, 3)
	
class Cylinder(Shape):
	def __init__(self, radius:float, height:float):
		self.radius = radius
		self.height = height

	def GetArea(self) -> float:
		return 2 * math.pi * self.radius * self.height + 2 * math.pi * pow(self.radius,2)
	
	def GetVolume(self) -> float:
		return math.pi * pow(self.radius, 2) * self.height
	
class Sphere(Shape):
	def __init__(self, radius:float):
		self.radius = radius

	def GetArea(self) -> float:
		return 4 * math.pi * pow(self.radius, 2)
	
	def GetVolume(self) -> float:
		return 4/3 * math.pi * pow(self.radius, 3)
	
class Prism(Polygon):
	def __init__(self, sideLength:float, sides:int, height:float):
		
		super().__init__(sideLength, sides)

		self.height = height
		self.surfaceArea = 2 * self.GetArea() + self.GetPerimeter() * self.height
		self.volume = self.GetArea() * self.height

	def GetVolume(self) -> float:
		return self.volume

	def GetSurfaceArea(self) -> float:
		return self.surfaceArea