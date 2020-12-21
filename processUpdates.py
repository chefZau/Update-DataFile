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