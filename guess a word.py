rules = print ("Welcome to guess word! The rules are simple. I will choose a word, and you will guess the letters. This is not hangman, so you will not be limited to just a few guesses. Are you ready? Let's go.")

import random 
words = ("sowpods.txt")
 
word = random.choice(words)
 
 
print("Guess the characters")