import os
from catalogue import *

def formatInput(textLine):
	"""
	the purpose of this funciton is to clean
	leading and trailing spaces, including 
	cases when multiple spaces separate words
	
	:param: textLine: the input text
	"""
	textLine = textLine.upper().strip()
	wordList = textLine.split()
	textLine = " ".join(wordList)
	
	return textLine


def capitalizeInput(sentence):
	"""
	This function will take a sentence(string), convert it to the proper format.
	The first character is capitalized.

	Note: SouthKorea will become SouthKorea,
	since we are only changing the first letter
	"""
	return " ".join(list(map(lambda x : x[0].upper() + x[1:], sentence.strip().split())))


def isValidNum(string):
	"""
	The purpose of this function is to check 
	whether the input number is valid or not.

	string: input number
	"""
	tmp = string.replace(",", "")
	if "." in tmp: return False
	try:
		tmp = int(tmp)
	except ValueError:
		return False
	return ("{:,}".format(int(tmp)) == string)


def isValidContinent(string):
	"""
	The purpose of this function is to check a string 
	is a valid continent on earth. If the string is valid, 
	return the formated version. Else return None.

	string: the string we want to check
	"""
	validContinent = {
		"AFRICA" : "Africa",
		"ANTARCTICA" : "Antarctica",
		"ARCTIC" : "Arctic",
		"ASIA" : "Asia",
		"EUROPE" : "Europe",
		"NORTH AMERICA" : "North America",
		"SOUTH AMERICA" : "South America"
	}
	tmp = formatInput(string)
	if tmp not in validContinent.keys(): return None
	return validContinent[tmp]


def log(fname, message):
	"""
	The purpose of this function is to
	log to a file.

	fname: file name
	message: the message you want to log
	"""
	file = None
	try:
		file = open(fname, "a")
	except:
		file = open(fname, "w")
	finally:
		file.write(message)
		file.close()


def checkValidUpdates(updates):
	"""
	The purpose of this function is to
	check whether every element in a list is 
	valid.

	updates: is a list
	"""
	for update in updates:

		if "=" not in update: return False

		L, value = update.split("=")
		L = L.strip()
		if L in ["P", "A"] and not isValidNum(value.strip()):
			return False
		elif L == "C" and not isValidContinent(value.strip()):
			return False

	return True


def promptUserFileName(fileName):
	"""
	If the fileName does not exist, keep asking until the user say N.
	else return fileName.

	fileName: the file you want to open
	"""

	while not os.path.exists(fileName):
		
		res = str(input("File does not exist. Quit? \"Y\"(yes) or \"N\"(no): "))

		if res == "N":
			fileName = str(input("Enter the name of the new file: ")) 

		else:
			log("output.txt", "Update Unsuccessful\n")
			return None

	return fileName


def processUpdates(cntryFileName, updateFileName):
	"""
	cntryFileName  : the name of a file containing country data, data.txt
	updateFileName : contain the name of a file containing updates.

	each record(row) specifies updates for a single country

	record format: Country;update1;update2;update3 
	update format: <L>=<value>
	L = {
		P : population,
		A : area,
		C : continent
	} 
	"""
	cntryFileName = promptUserFileName(cntryFileName)
	if not cntryFileName: return False

	updateFileName = promptUserFileName(updateFileName)
	if not updateFileName: return False

	cntries = CountryCatalogue(cntryFileName)
	queries = open(updateFileName, "r", encoding="utf-8").readlines()

	for query in queries:

		cnName, *updates = query.strip().split(";")
		
		cnName = capitalizeInput(cnName)

		if not updates: 
			print("No Updates for Country: ", cnName)
			continue

		# if updates not valid or no updates, skip the row
		if not checkValidUpdates(updates[:3]): 
			print("Invalid Query for Country: ", cnName, *updates, sep=" ")
			continue

		# if country not exists, create new country with empty value
		if not cntries.findCountry(cnName):
			cntries.addCountry(cnName, "", "", "")
		
		for update in updates[:3]:

			L, value = update.split("=")

			if L.strip() == "P": 
				cntries.setPopulationOfCountry(cnName, value.strip())
			elif L.strip() == "A":
				cntries.setAreaOfCountry(cnName, value.strip())
			elif L.strip() == "C":
				cntries.setContinentOfCountry(cnName, isValidContinent(value.strip()))

	cntries.saveCountryCatalogue("output.txt")
	return True


