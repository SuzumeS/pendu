import os
import pickle
import random


def dictionnary_size():
	#This function should only be called when the dictionnary has been updated 
	with open("words.txt", "r") as mon_fichier:
		for i,l in enumerate(mon_fichier):
			pass
		print("The dictionnary size contains {0} words").format(i)
	return(i)



def random_start(size):
	

	randomNumber = random.randint(0,size)
	print("Searching for a new word at position {0}").format(randomNumber)
	with open("words.txt", "r") as mon_fichier:
		for i,word in enumerate(mon_fichier):
			if i == randomNumber:
				break
	print(word) 
	return word

#launching all
mysize = dictionnary_size();
guess_word = random_start(mysize);


