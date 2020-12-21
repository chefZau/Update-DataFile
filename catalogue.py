from country import	*

class CountryCatalogue(object):

	def __init__(self, countryFile):
		
		self.countryCat = dict()

		data = open(countryFile, "r", encoding="utf-8").readlines()

		for line in data[1:]:
			name, continent, pop, area = line.strip().split("|")
			countryObj = Country(name, pop, area, continent)
			self.countryCat[name] = countryObj