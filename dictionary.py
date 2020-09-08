import json
from difflib import get_close_matches as get_them

data = json.load(open("dictionary.json"))

def translate (word):
	word = word.lower()
	if word in data.keys():
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_them(word, data.keys())) > 0:
		yesno = input("Did you mean %s instead? Enter 'Yes' if yes or 'No' if no: " %get_them(word, data.keys())[0])
		yesno = yesno.lower()
		if yesno == "yes":
			return data[get_them(word, data.keys())[0]]
		elif yesno == "no":
			return "Entry not understood. Please try again"
		else:
			return "The word does not exist"
	else:
		return "The word does not exist"
	
word = input("Enter a word: ")

output = (translate(word))

if type(output) == list:
	for meaning in output:
		print(meaning)
else:
	print(output)
