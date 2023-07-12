# https://realpython.com/python-wordle-clone/#project-overview

import sys
import pathlib
import random
from string import ascii_letters



def main():
	word = generate_word()
	play_game(word)
	game_over(word)

def generate_word():
	wordlist = pathlib.Path("wordlist.txt")
	wordlist = [word.upper()
	for word in wordlist.read_text(encoding="utf-8").split("\n")
	if len(word) == 5 and all(letter in ascii_letters for letter in word)
	]
	print(wordlist)
	return random.choice(wordlist)

def play_game(word):
	for num_guess in range(1,7):
		guess = input(f"Guess {num_guess}: ").upper()
	
		if guess == 'EXIT':
			sys.exit()

		if guess == word:
			print("correct")
			break

		correct_lets = {guess_letter for guess_letter, correct_letter in zip(guess, word) if guess_letter == correct_letter}
		misplaced_lets = set(guess) & set(word) - correct_lets
		wrong_lets = set(guess) - set(word)
		print("correct letters: ", ", ".join(sorted(correct_lets)))
		print("misplaced_letters: ", ", ".join(sorted(misplaced_lets)))
		print("wrong_letters: ", ", ".join(sorted(wrong_lets)))
		
		print(f'Your guess, {guess}, is incorrect. You have {6-num_guess} guesses remaining.')


def game_over(word):
	print(f'the word was: {word}')
	play_again = input(f"Do you want to play again (Yes/no) ").upper()
	if play_again == "YES":
		main()
	else:
		sys.exit()

if __name__ == '__main__':
	main()
