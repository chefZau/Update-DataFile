from country import	*

class CountryCatalogue(object):

	def __init__(self, countryFile):
		
		self.countryCat = dict()

		data = open(countryFile, "r", encoding="utf-8").readlines()

		for line in data[1:]:
			name, continent, pop, area = line.strip().split("|")
			countryObj = Country(name, pop, area, continent)
			self.countryCat[name] = countryObj

	
	def setPopulationOfCountry(self, countryName, newPop):
		if countryName in self.countryCat.keys():
			self.countryCat[countryName].setPopulation(newPop)

	def setAreaOfCountry(self, countryName, newArea):
		if countryName in self.countryCat.keys():
			self.countryCat[countryName].setArea(newArea)

	def setContinentOfCountry(self, countryName, newContinent):
		if countryName in self.countryCat.keys():
			self.countryCat[countryName].setContinent(newContinent)

	def findCountry(self, country):
		if country not in self.countryCat.keys():
			return None
		return self.countryCat[country]