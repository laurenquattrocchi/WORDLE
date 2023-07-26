# https://realpython.com/python-wordle-clone/#project-overview

import sys
import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme
# example
# console = Console()
# console.print("Hello, [bold red]Rich[/] :snake:")
# console = Console(width=40, theme=Theme({"warning": "red on yellow"}))
console = Console(theme=Theme({"warning": "red on yellow"}))


def main():
	wordlist =  pathlib.Path(__file__).parent / "wordlist.txt"
	word = generate_word(wordlist.read_text(encoding="utf-8").split("\n"))
	# initiate lst to track guesses
	guesses = ["_" * 5] * 6
	
    # process (mian loop)
	for num_guess in range(6):
		refresh_page(headline=f"Guess {num_guess + 1}")
		show_guesses(guesses, word)
		#show guess before getting new guess b/c refresh_page() clears screen 
		guesses[num_guess] = input(f"Guess: ").upper()
		# quick exit for testing
		if guesses[num_guess] == 'EXIT':
			sys.exit()
		validate_guess(guesses, num_guess)
		if guesses[num_guess] == word:
			break

	# post-process
	game_over(word, guesses[num_guess] == word, guesses)

def generate_word(wordlist):
	'''
	input: None
	returns: None
	generates random word for wordlist.txt

	test:
	"""Get a random five-letter word from a list of strings.

    ## Example:

    >>> generate_word(["snake", "worm", "it'll"])
    'SNAKE'
    """
	'''
	
	wordlist = [word.upper()
	for word in wordlist
		if len(word) == 5 and all(letter in ascii_letters for letter in word)
	]
	# print(wordlist)
	return random.choice(wordlist)

def show_guesses(guesses, word):
	'''	input: randomly generated word to be guessed
	output: None
	takes user input guesses and prints # of remaining guesses and letter analysis
	
	test example: run with python -m doctest -v main.py
	>>> show_guess("CRANE", "SNAKE")
	correct letters:  A, E
	misplaced letters:  N
	wrong letters:  C, R
	'''

	for guess in guesses:
		styled_guess = []
		# wrap each guess in markup block w/ appropriate color for level of correctness
		# loop over the letters in the guess and in the secret word in parallel using zip().
		for guess_letter, correct_letter in zip(guess, word):
			if guess_letter == correct_letter:
				style = "bold white on green"
			elif guess_letter in word:
				style = "bold white on yellow"
			elif guess_letter in ascii_letters:
				style = "white on #666666"
			else:
				style = "dim"
			styled_guess.append(f"[{style}]{guess_letter}[/]") 

		console.print("".join(styled_guess), justify="center")
			# misplaced_lets = set(guess) & set(word) - correct_lets
			# wrong_lets = set(guess) - set(word)
			# print("correct letters: ", ", ".join(sorted(correct_lets)))
			# print("misplaced letters: ", ", ".join(sorted(misplaced_lets)))
			# print("wrong letters: ", ", ".join(sorted(wrong_lets)))
			
			#print(f'Your guess, {guess}, is incorrect. You have {6-num_guess} guesses remaining.')


def game_over(word, correct, guesses):
	'''
	input: randomly generated word to be guessed
	output: None
	if user wants to play again calls main, otherwise exits shell
	'''

	show_guesses(guesses, word)
	if correct:
		headline = "Congratulations, you win"
	else:
		headline = f"Game over, the correct word was {word}"

	console.rule(f"[bold blue] :leafy_green: {headline} :leafy_green:[/]\n")
	play_again = input(f"Do you want to play again (Yes/no) ").upper()
	if play_again == "YES":
		main()
	else:
		sys.exit()

def refresh_page(headline):
	console.clear()
	console.rule(f"[bold blue] :leafy_green: {headline} :leafy_green:[/]\n")

def validate_guess(guesses, num_guess):
	guess = guesses[num_guess]
	#check if guess isn't 5 letters
	if len(guess) != 5:
		console.print("Try again, guesses need to be 5 letter words", style = "warning")
		guesses[num_guess] = input(f"Guess: ").upper()
		# quick exit for testing
		if guesses[num_guess] == 'EXIT':
			sys.exit()
		return validate_guess(guesses, num_guess)

	# check if duplicate guess
	elif guess in guesses[:num_guess]:
		console.print("Try again, you already guessed this word", style = "warning")
		guesses[num_guess] = input(f"Guess: ").upper()
		# quick exit for testing
		if guesses[num_guess] == 'EXIT':
			sys.exit()
		return validate_guess(guesses, num_guess)

	#check if 



if __name__ == '__main__':
	main()
