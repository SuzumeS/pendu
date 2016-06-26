import os
import pickle
import random

# A implementer
# - Prendre en parametres une liste de pokemon
# - Mettre en place le vrai décompte des erreurs et refixer le total disponible + afficher score final






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


def compute_result(trials, word):
	result = []
	for letter in word:
		hypothesis = False
		for trial in trials:
			if letter==trial:
				hypothesis = True
		if hypothesis:
			result.append(letter)
		else:
			result.append("_")
	return result

	


#This fonction describes the game process
def game_on(input_word):
	reframe_input = input_word[:-1].lower() #Used to remove the last character
	number_of_characters = len(reframe_input);
	print("Le mot a trouver contient {0} caracteres").format(number_of_characters);
	for lettre in reframe_input:
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
		#Checking if the user has won
		if len(the_trials) != 0:
			if ''.join(compute_result(the_trials, reframe_input)) == reframe_input:
				print("GG!!!!!!!!!")
				game_over = True
				break
		#Checking if the user has lost
		if len(the_trials)==10:
			print("Game over")
			game_over = True
		else: #Go on with the game
			#Display results so far
			if len(the_trials)==0:
				print("Premier essai")
			else:
				current_state = compute_result(the_trials, reframe_input)
				print(current_state)
				print("Vous avez essaye les lettres suivantes : ")
				print(" ".join(the_trials))
			print("Il vous reste {nb_restant} essais").format(nb_restant=10-len(the_trials))

			#Ask for user input
			while True: #The while loop checks that user's input is correct
				user_input = raw_input('Merci dentrer une lettre : ')
				if type(user_input) != str:
					print("Vous navez pas entrer une chaine de caracteres")
					continue
				elif len(user_input) != 1:
					print("Vous avez entrer plus d'une lettre")
					continue
				elif user_input.lower() in the_trials:
					print("Vous avez deja entre ce caractere")
					continue
				else:
					print("Votre input est correct")
					break
			user_input = user_input.lower()
			the_trials.append(user_input)
			if user_input in reframe_input:
				print("La lettre est bien dans le mot a deviner")
			else:
				print("DOMMAGE! La lettre n'est pas dans le mot")
			print("Tour fini")
			print
			print("----------------------------------------------------------------")
			print




#launching all
mysize = dictionnary_size();
guess_word = random_start(mysize);
game_on(guess_word);



