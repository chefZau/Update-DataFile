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

	def addCountry(self, countryName, pop, area, cont):
		if countryName in self.countryCat.keys(): return False

		tmpCountry = Country(countryName, pop, area, cont)
		self.countryCat[countryName] = tmpCountry
		return True

	def printCountryCatalogue(self):
		for _, countryObj in self.countryCat.items():
			print(countryObj)

	def saveCountryCatalogue(self, fname):
		# save all country information in the catalogue to a file
		lines = "Country|Continent|Population|Area\n"
		count = 0

		for countryName, countObj in sorted(self.countryCat.items()):
			lines += "{}|{}|{}|{}\n".format(countryName, countObj.getContinent(), countObj.getPopulation(), countObj.getArea())
			count += 1
		
		try:
			outF = open(fname, "w")
			outF.writelines(lines)
			return count
		
		except:
			return -1
		
		finally:
			outF.close()