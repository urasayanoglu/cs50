import string
punctuations = string.punctuation

def testme(arguement):
	if len(arguement) < 6 or arguement.isdigit() or arguement.isalpha() or arguement in punctuations:
		return False
	elif len(arguement) >= 6 and arguement.isalnum():
		return True

