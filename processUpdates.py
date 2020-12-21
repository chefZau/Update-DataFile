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