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