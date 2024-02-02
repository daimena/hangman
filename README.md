# Hangman Game

A simple Hangman game developed in Python as part of the [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) problem set.

## Description

The Hangman game is a classic word-guessing game. The computer selects a secret word at random from the list of available words in `words.txt` and provides the user with the number of letters in the word. The user has to guess the letters one at a time, and the computer provides feedback after each guess.

## How to Play

1. Run the Python file.
2. The computer randomly selects a secret word and informs you of the number of letters.
3. Before each guess, the computer displays the number of remaining guesses and the available letters.
4. Enter one letter at a time for each guess.
5. The computer indicates whether the guessed letter is in the word and displays the secret word with underscores for unrevealed letters.
6. If the guessed letter is not in the word, the user loses a guess. The game continues until the user guesses all the letters or runs out of guesses.

## Rules for Input

1. The user starts with 3 warnings.
2. Only alphabets are allowed. Any other input results in a warning or loss of a guess.
3. Repeated letters result in a warning or loss of a guess, depending on the situation.
4. Consonants that haven't been guessed result in a loss of one guess if incorrect.
5. Vowels that haven't been guessed result in a loss of two guesses if incorrect.

## Features

- Interactive command-line interface.
- Random selection of words from `words.txt`.
- Input validation and handling according to specified rules.

## Example implementation

1. Clone the repository and run the Hangman game Python file.

```bash
git clone https://github.com/daimena/hangman.git
cd hangman-game
python hangman.py
```

2. Run the Hangman game Python file:
```
python hangman.py
```

3. Follow the on-screen instructions to play the game. For example:
```
Loading word list from file...
   55900 words loaded.

Welcome to the game Hangman!
I am thinking of a word that is 9 letters long.
          

----------------------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz            
              
Please guess a letter: e
Good guess!: _ _ _ _ _ _ _ e_ 

----------------------
You have 6 guesses left.
Available letters: abcdfghijklmnopqrstuvwxyz            
              
Please guess a letter: x
Oops! That letter is not in my word: _ _ _ _ _ _ _ e_ 

----------------------
You have 5 guesses left.
Available letters: abcdfhijklmnopqrstuvwyz 
```