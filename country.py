class Country(object):

	def __init__(self, name, pop, area, continent):
		self.name = name
		self.pop = pop
		self.area = area
		self.continent = continent

	def getName(self):
		return self.name

	def getPopulation(self):
		return self.pop

	def getArea(self):
		return self.area

	def getContinent(self):
		return self.continent