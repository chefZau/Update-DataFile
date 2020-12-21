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

	def setPopulation(self, newPop):
		self.pop = newPop

	def setArea(self, newArea):
		self.area = newArea

	def setContinent(self, newCont):
		self.continent = newCont

	def __repr__(self):
		# Name (pop: population value, size: area value) in Continent
		return "{} (pop: {}, size: {}) in {}".format(self.name, self.pop, self.area, self.continent)