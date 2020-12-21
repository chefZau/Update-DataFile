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