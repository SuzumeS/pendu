import os
import pickle
import random

#This function should only be called when the dictionnary has been updated 
def dictionnary_size():
	
	with open("words.txt", "r") as mon_fichier:
		for i,l in enumerate(mon_fichier):
			pass
		print("The dictionnary size contains {0} words").format(i)
	return(i)


#This function looks for a random entry in the dictionnary and returns it
def random_start(size):
	randomNumber = random.randint(0,size)
	print("Searching for a new word at position {0}").format(randomNumber)
	with open("words.txt", "r") as mon_fichier:
		for i,word in enumerate(mon_fichier):
			if i == randomNumber:
				break
	print(word) 
	return word




#This fonction describes the game process
def game_on(input_word):
	number_of_characters = len(input_word);
	print("Le mot a trouver contient {0} caracteres").format(number_of_characters-1);
	for lettre in input_word:
		print("_ "),
	print
	print("----------------------------------------------------------------")
	print
	game_over = False
	the_trials = []
	print(len(the_trials))
	
	#While loop as the game goes on
	#TBContinued : the checking system is the hardest part obviously
	while not game_over:
		if len(the_trials)==0:
			print("Premier essai")
		else:
			for el in the_trials:
				if el in input_word:
					the_positions 	

		print("OK")
		game_over = True





#launching all
mysize = dictionnary_size();
guess_word = random_start(mysize);
game_on(guess_word);



